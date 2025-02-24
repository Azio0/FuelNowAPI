import os
import requests
import json

os.makedirs('../utils/api/worker-output', exist_ok=True)

with open('../utils/api/datasets.json', 'r') as dataFile:
    dataJSON = json.load(dataFile)

def UpdateFuelPrice():
    for entry in dataJSON:
        try:
            response = requests.get(entry['url'], timeout=10)

            if response.status_code == 200:
                data = response.json()
                company_name = entry['company'].lower()
                company_filename = f'../utils/api/worker-output/{company_name.replace(' ', '_').replace('/', '_')}.json'

                with open(company_filename, 'w') as company_file:
                    json.dump(data, company_file, indent=4)
            else:
                print(f'[Worker Error] Failed to fetch data from {entry['company']}.')

        except Exception as error:
            print(f'[Worker Error] {error}.')

    return '[Worker] Fuel prices updated.'

def RecoverFuelPriceByCom(company_name):
    try:
        folder_path = "../utils/api/worker-output/"
        file_path = os.path.join(folder_path, f'{company_name}.json')
    
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                company_data = json.load(file)

            return company_data, 200
        
        else:
            return f"[Worker Error] The API was unable to recover data for company name {company_name}", 404

    except Exception as error:
        return f'[Worker Error] {error}.', 500