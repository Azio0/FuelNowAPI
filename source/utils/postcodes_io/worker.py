import requests

def PostcodeInformation(postcode):
    try:
        response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}', timeout=10)

        if response.status_code == 200:
            return response.json(), 200
        
        else:
            raise Exception('The postcode provided is not valid, please check your input')

    except Exception as error:
        return f'[Worker Error] {error}.', 500

def ValidatePostcode(postcode):
    try:
        response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}/validate', timeout=10)

        if response.status_code == 200:
            return response.json(), 200
        
        else:
            raise Exception('The postcode provided is not valid, please check your input')

    except Exception as error:
        return f'[Worker Error] {error}.', 500
    
def RecoverPostcodeCity(postcode):
    try:
        status, result = ValidatePostcode(postcode)
        if status['result'] == True:
            response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}', timeout=10)

            if response.status_code == 200:
                data = response.json()
                city = data['result']['admin_district']

                return city, 200

            else:
                raise Exception('The API was unable to recover data for your request')
            
        else:
                raise Exception('The postcode provided is not valid, please check your input')

    except Exception as error:
        return f'[Worker Error] {error}.', 500
    
def RecoverPostcodeCounty(postcode):
    try:
        status, result = ValidatePostcode(postcode)
        if status['result'] == True:
            response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}', timeout=10)

            if response.status_code == 200:
                data = response.json()
                county = data['result']['admin_county']

                return county, 200

            else:
                raise Exception('The API was unable to recover data for your request')
            
        else:
                raise Exception('The postcode provided is not valid, please check your input')

    except Exception as error:
        return f'[Worker Error] {error}.', 500
    
def BulkPostcodeQuery(postcodes):
    try:
        payload = {
            "postcodes": postcodes
        }
        response = requests.post('https://api.postcodes.io/postcodes', json=payload, timeout=10)

        if response.status_code == 200:
            data = response.json()

            return data, 200
        
        else:
            raise Exception('The API was unable to recover data for your request')

    except Exception as error:
        return f'[Worker Error] {error}.', 500
