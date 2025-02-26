import json

with open('../utils/filters/filter-caller.json', 'r') as filterFile:
    filterJSON = json.load(filterFile)

def RecoverFilterParms(filter_parm):
    try:
        for entry in filterJSON:
            if entry['name'] == filter_parm:
                return entry['exec_command'], 200

        return f'[Worker Error] The filter worker was unable to recover data for paramanater {filter_parm}.', 404
        
    except Exception as error:
        return f'[Worker Error] {error}.', 500
