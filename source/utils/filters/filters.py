def Outcode_Only(data, postcode):
    return [station for station in data["stations"] if station["postcode"].split(" ")[0] == postcode]
