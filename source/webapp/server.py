import os
import sys
import yaml
import json
from flask import Flask, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.api.worker import UpdateFuelPrice
from utils.api.worker import RecoverFuelPriceByCom

app = Flask(__name__)

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

def startup():
    UpdateFuelPrice()

@app.route('/api/v1/', methods=['GET'])
def api_landing():
    data = {
        'type': 'Information',
        'message': 'Welcome to the FuelNow API.',
        'routes': config['api']['routes'],
    }
    return jsonify(data)

@app.route('/api/v1/com/<company>', methods=['GET'])
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
