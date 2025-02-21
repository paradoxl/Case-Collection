from thehive4py import TheHiveApi
import os
from dotenv import load_dotenv
import json


load_dotenv()

def collectAllCases():
    api_key = os.getenv('THEHIVE_API_KEY')
    hive_url= os.getenv('THEHIVE_URL')
    hive = TheHiveApi(hive_url, apikey=api_key)
    case_load = []
    i = 0
    while i < 648:
        try:
            print("checking case: " + str(i))
            fetched_case = hive.case.get(case_id=i)
            case_load.append(fetched_case)
            i += 1
        except Exception as e:
            print("whoops an exception occurred: " + str(e))
            i += 1
            continue
    
    # Write the results to a file
    with open('case_load.json', 'w') as file:
        json.dump(case_load, file, indent=4)
    
    print("Cases have been written to case_load.json")

if __name__ == '__main__':
    collectAllCases()