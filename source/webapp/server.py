import os
import sys
import yaml
from flask import Flask, redirect, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.api.worker import UpdateFuelPrice
from utils.api.worker import RecoverFuelPriceByCom
from utils.filters.worker import RecoverFilterParms
from utils.filters.filters import Outcode_Only, Incode_Only, City
from utils.redis.worker import SetupRedis

app = Flask(__name__)
redis_client, limiter = SetupRedis(app)

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

def startup():
    UpdateFuelPrice()

@app.route('/', methods=['GET'])
@limiter.limit("10/minute")
def index():
    return redirect('/api/v1/', code=307)

@app.route('/api/v1/', methods=['GET'])
@limiter.limit("10/minute")
def api_landing():
    data = {
        'type': 'Information',
        'message': 'Welcome to the FuelNow API.',
        'routes': config['api']['routes'],
    }
    return jsonify(data)

@app.route('/api/v1/com/<company>', methods=['GET'])
@limiter.limit("10/minute")
def api_com_lookup(company):
    company_name = company.lower().replace(' ', '_').replace('/', '_')
    company_data, status_code = RecoverFuelPriceByCom(company_name)

    if status_code == 200:
        return company_data

    else:
        data = {
            'type': 'Error',
            'message': f'The API was unable to recover data for company name {company}.'
        }

        return jsonify(data)

@app.route('/api/v1/com/<company>/filter/<filter>/postcode/<postcode>')
@limiter.limit("10/minute")
def api_com_filter_lookup(company, filter, postcode):
    company_name = company.lower().replace(' ', '_').replace('/', '_')
    company_data, status_code_rfpbc = RecoverFuelPriceByCom(company_name)

    filter = filter.lower().replace('-', '_')
    command, status_code_rfp = RecoverFilterParms(filter)
    
    if status_code_rfpbc and status_code_rfp == 200:
        filtered_data = jsonify(eval(command))

        return filtered_data

    else:
        data = {
            'type': 'Error',
            'message': f'The API was unable to recover data for your request, please check the company name and filter.'
        }

        return jsonify(data)
    
@app.errorhandler(Exception)
def api_error_handle(error):
    data = {
        'type': 'Error',
        'message': 'An error occured causing your request to be dropped.',
        'error_data': str(error)
    }

    return jsonify(data)

if __name__ == '__main__':
    startup()

    portToggle=5000
    debugToggle=False

    if config['app']['environment'] == 'development':
        debugToggle=True

    if config['app']['port'] != 'default':
        portToggle = config['app']['port']

    app.run(debug=debugToggle, port=portToggle)
