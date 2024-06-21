#Get data from open weather, return data to post on twitter
import requests
import aiohttp


class WeatherMange():
    """Open Weather Api management"""

    @staticmethod
    #connect to specific endpoint to check if it's working
    def check_api(ApiKey:str) -> None:
        """Check if open weather api works"""
        print('Checking Open Weather API status..')
        for_counter = 0
        for x in range(5):
            try:
                r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={ApiKey}')
                if r.status_code == 200:
                    print('Connection established to Open Weather API ...')
                    break
                elif r.status_code != 200:
                    for_counter += 1
                    raise exceptions.HTTPError(r.status_code)

            except exceptions.HTTPError as e:
                print(f'Cannot establish connection to server error, trying {for_counter}, error {e}...')
                if for_counter == 5:
                    break

    #Async function to get data from a given URL using aiohttp
    @staticmethod
    async def call_api(session: aiohttp.ClientSession,city:str, api_key:str):
        """Call Open Weather Api """
        api_call: str = 'https://api.openweathermap.org/data/2.5/weather?q={CityName}&&units=metric&lang=pl&appid={ApiKey}'
        api_call: str = api_call.replace('{CityName}',city).replace('{ApiKey}',api_key)
        print(f'Requesting {api_call}')

        #Use session.get() to make an async HTTP GET request
        async with session.get(api_call) as response:
            try:
                if response.status == 404:
                    print(f'Status -> {response.status}')
                    raise requests.HTTPError(response.status)

                return await response.json()
            except Exception as e:
                print(f'Error with URL {response.url}, error -> {e}')

    @staticmethod
    async def prepare_data(city_json: dict) -> dict:
        """Prepare data for further processing"""
        city_data: dict = {}

        if city_json['name'] == 'Województwo opolskie':
            city_data['city_name'] = 'Opole'
        elif city_json['name'] == 'Województwo lubelskie':
            city_data['city_name'] = 'Lublin'
        else:
            city_data['city_name'] = city_json['name']

        city_data['weather_dsc'] = city_json['weather'][0]['description']
        city_data['temp_min'] = city_json['main']['temp_min']
        city_data['temp_max'] = city_json['main']['temp_max']
        city_data['temp_act'] = city_json['main']['temp']
        city_data['temp_feels'] = city_json['main']['feels_like']
        city_data['humidity'] = city_json['main']['humidity']
        city_data['pressure'] = city_json['main']['pressure']
        return city_data