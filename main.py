# Written for STGen Cybersecurity department
# Author: Michael Evans 2025

# TODO:
# fix time/date - Complete
# fix case #
# determine a way to find last case and automatically pull whole list

from thehive4py import TheHiveApi
import os
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

# This function will collect all cases from TheHive and write them to a json file
def collectAllCases():
    api_key = os.getenv('THEHIVE_API_KEY')
    hive_url= os.getenv('THEHIVE_URL')
    hive = TheHiveApi(hive_url, apikey=api_key)
    case_load = []
    i = 0
    while i < 666:
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

# converts epoch time to human readable time
def convert_epoch_to_human_readable(epoch):
    return datetime.fromtimestamp(epoch / 1000).strftime('%Y-%m-%d %H:%M:%S')

# This function will update the dates in the json file to be human readable
def update_dates_in_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Changes startDate and endDate
    for case in data:
        if 'startDate' in case:
            try:
                case['startDate'] = convert_epoch_to_human_readable(case['startDate'])
            except Exception as e:
                print(f"Error converting startDate for case {case}: {e}")
        if 'endDate' in case:
            try:
                case['endDate'] = convert_epoch_to_human_readable(case['endDate'])
            except Exception as e:
                print(f"Error converting endDate for case {case}: {e}")

        # Changes created and updated
        if '_createdAt' in case:
            try:
                case['_createdAt'] = convert_epoch_to_human_readable(case['_createdAt'])
            except Exception as e:
                print(f"Error converting startDate for case {case}: {e}")
        if '_endDate' in case:
            try:
                case['_updatedAt'] = convert_epoch_to_human_readable(case['_updatedAt'])
            except Exception as e:
                print(f"Error converting endDate for case {case}: {e}")

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Case dates have been altered from Epoch to standard date/time format")


if __name__ == '__main__':
    # collectAllCases()
    # print("Blurb")
    update_dates_in_json('case_load.json')