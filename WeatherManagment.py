import requests
import json
from abc import ABC, abstractmethod
from urllib.error import HTTPError


class WeatherManageTemplate(ABC):

    @abstractmethod
    def GetDataFromJson() -> dict:
        ...
    @abstractmethod
    def CheckApi() -> None:
        ...

    @abstractmethod
    def GetCityListy()-> list:
        ...

    @abstractmethod
    def CheckApiStatus() -> None:
        ...

    @abstractmethod
    def GetWeatherPerCity() -> str:
        ...


class WeatherMange(WeatherManageTemplate):

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
                r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={ApiKey}')
                print(r.status_code)

                if r.status_code == 200:
                    print('Connection established...')
                    boolFlag = False
                elif counter < 5:
                    print(f'Could not establish connection, try -> {str(counter)}')
                elif counter == 5:
                    boolFlag = False
                    raise requests.exceptions.HTTPError

        except requests.exceptions.HTTPError as e:
            print(f'Cannot establish connection to server error...')

    @staticmethod
    def GetCityListy(ApiKey:str) -> list:
        print(ApiKey)

    def CheckApiStatus() -> None:
        ...

    def GetWeatherPerCity() -> str:
        ...


c = WeatherMange()
a = c.GetDataFromJson()
b = c.CheckApi(a['apiKey'])
#c.GetCityListy(a)

