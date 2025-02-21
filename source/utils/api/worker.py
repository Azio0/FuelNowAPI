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
