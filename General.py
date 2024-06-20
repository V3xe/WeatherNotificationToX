#General purpose functions
import json

class misc_functions():
    #reading data from JSON file
    @staticmethod
    def get_data_from_json() -> dict:
        print('Getting data from JSON...')
        with open('config.json', 'r') as f:
            data: dict = json.load(f)
            return data

