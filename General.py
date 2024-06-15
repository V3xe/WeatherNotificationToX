#General purpose functions
import json

class General():
    #reading data from JSON file
    @staticmethod
    def GetDataFromJson() -> dict:
        print('Getting data from JSON...')
        file = open('config.json')
        data = json.load(file)
        file.close()
        return data

