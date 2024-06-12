import requests
import json
from abc import ABC, abstractmethod


class WeatherManageTemplate(ABC):

    @abstractmethod
    def GetDataFromJson() -> dict:
        ...
    @abstractmethod
    def CheckApi() -> None:
        ...

    @abstractmethod
    def GetWeatherPerCity() -> str:
        ...


class WeatherMange(WeatherManageTemplate):
    ApiCall: str = 'https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid={ApiKey}'
    @staticmethod
    #reading data from JSON file
    def GetDataFromJson() -> dict:
        print('Getting data from JSON...')
        file = open('config.json')
        data = json.load(file)
        file.close()
        return data

    @staticmethod
    #connect to specific endpoint to check if it's working
    def CheckApi(ApiKey:str) -> None:
        print('Checking API status..')
        boolFlag: bool = True
        counter: int = 0
        try:
            while boolFlag:
                counter += 1
                r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={ApiKey}')
                if r.status_code == 200:
                    print(f'Connection established, status {r.status_code}...')
                    boolFlag = False
                elif counter < 5:
                    print(f'Could not establish connection, error {r.status_code}, try -> {str(counter)}')
                elif counter == 5:
                    raise requests.exceptions.HTTPError

        except requests.exceptions.HTTPError as e:
            print(f'Cannot establish connection to server error, {e}...')

    #@staticmethod
    #get city list
    #def GetCityListy(cityList: list) -> list:
    #    print(cityList)
    #    return cityList

    @staticmethod
    # Think of async request, send all requests and gather responses later?
    def GetWeatherPerCity(ApiCall: str, ApiKey: str, cityList: list) -> dict:
        for city in cityList:
            call = ApiCall.replace('{CityName}',city).replace('{ApiKey}',ApiKey)
            r = requests.get(call)
            print(r.json())
            print(call)
            print(f'{ApiCall}, {ApiKey}, {cityList}')



WeatherObject = WeatherMange()
ConfigJSON: dict = WeatherObject.GetDataFromJson()
print(ConfigJSON)
WeatherObject.CheckApi(ConfigJSON['apiKey'])
WeatherObject.GetWeatherPerCity(WeatherMange.ApiCall,ConfigJSON['apiKey'],ConfigJSON['cityList'])


#c.GetCityListy(a)

