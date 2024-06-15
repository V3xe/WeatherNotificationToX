#Get data from open weather, return data to post on twitter
import requests
import json

class WeatherMange():
    ApiCall: str = 'https://api.openweathermap.org/data/2.5/weather?q={CityName}&&units=metric&lang=pl&appid={ApiKey}'

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
    @staticmethod
    def getCityDataFromResponse(keyFromList: list | dict,cityWeather: dict,newDictKey: str,dictKeyValue:str) -> dict:
        if type(keyFromList) == list:
            KeyDict: dict = keyFromList[0]
            cityWeather[newDictKey] = KeyDict[dictKeyValue]
            #print(KeyDict)
            return cityWeather
        elif type(keyFromList) == dict:
            cityWeather[newDictKey] = dictKeyValue
            return cityWeather

    @staticmethod
    # Think of async request, send all requests and gather responses later?
    def GetWeatherPerCity(ApiCall: str, ApiKey: str, city) -> dict:
            cityWeather: dict = {}
            call = ApiCall.replace('{CityName}',city).replace('{ApiKey}',ApiKey)
            cityWeather['cityName'] = city
            r = requests.get(call)
            data: dict = r.json()
            #print(data)
            WeatherMange.getCityDataFromResponse(data.get('weather'),cityWeather,'weather','description')
            r = data.get('main')
            WeatherMange.getCityDataFromResponse(data.get('main'),cityWeather,'temperature',r['temp'])
            WeatherMange.getCityDataFromResponse(data.get('main'),cityWeather,'tempFell',r['feels_like'])
            WeatherMange.getCityDataFromResponse(data.get('main'),cityWeather,'tempMin',r['temp_min'])
            WeatherMange.getCityDataFromResponse(data.get('main'),cityWeather,'tempMax',r['temp_max'])
            WeatherMange.getCityDataFromResponse(data.get('main'),cityWeather,'humidity',r['humidity'])
            #print(cityWeather)
            return cityWeather




