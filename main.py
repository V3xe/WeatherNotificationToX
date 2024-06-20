from WeatherManagment import WeatherMange
from TwitterIntegration import TwitterManagement
from General import misc_functions
import asyncio
import aiohttp

async def main() -> None:
    weather: object = WeatherMange()
    twitter: object = TwitterManagement()
    config_json: dict = misc_functions.get_data_from_json()

    #Check if Open Weather Api works
    weather.check_api(config_json['apiKeyOpenWeather'])

    #Check if Twitter Api works
    client: object = TwitterManagement.client_auth(config_json['bearerTokenTweeter'],
                                                     config_json['apiKeyTweeter'],
                                                     config_json['apiSecretTweeter'],
                                                     config_json['accessTokenTweeter'],
                                                     config_json['accessTokenSecretTweeter']
                                                     )

    #Call Open Weather Api, create an aiohttps ClientSession for making async HTTP requests
    async with aiohttp.ClientSession() as session:
        #Create list of tasks, where each task is call to 'call_api' with specific URL
        tasks: list[str] = [weather.call_api(session,city,
                                             config_json['apiKeyOpenWeather'])
                            for city in config_json['city_list']]
        city_data = await asyncio.gather(*tasks)

    #Get data from responses
        print('Preparing data from Open Weather API...')
        tasks: list[dict] = [weather.prepare_data(city) for city in city_data]
        processing_data = await asyncio.gather(*tasks)
        #print(processing_data)

    #Prepare data for twitter
        print('Preparing bodies for twitter...')
        tasks: list[dict] = [twitter.prepare_twitter(desc, config_json=config_json) for desc in processing_data]
        twitter_bodies = await asyncio.gather(*tasks)

    #Post to twitter
        print('Preparing bodies for twitter...')
        for item in twitter_bodies:
            print('-----')
            print(item)

        tasks: list[dict] = [twitter.create_twitter(client=client,twitter_body=body) for body in twitter_bodies]
        asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
