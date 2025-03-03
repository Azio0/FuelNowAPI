from utils.postcodes_io.worker import RecoverPostcodeCity

def Outcode_Only(data, postcode):
    postcode = postcode.split(' ')[0]
    return [station for station in data['stations'] if station['postcode'].split(' ')[0] == postcode]

def Incode_Only(data, postcode):
    postcode = postcode.split(' ')[1]
    return [station for station in data['stations'] if station['postcode'].split(' ')[1] == postcode]

def City(data, postcode):
    city, status = RecoverPostcodeCity(postcode)
    return [station for station in data['stations'] if station['address'].rsplit(',', 1)[-1].split(" ")[1] == city]
