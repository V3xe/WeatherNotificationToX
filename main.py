import WeatherManagment as WM
import TwitterIntegration as TI
import General

def main():
    weather: object = WM.WeatherMange()
    ConfigJSON: dict = General.General.GetDataFromJson()
    weather.CheckApi(ConfigJSON['apiKeyOpenWeather'])

    counter:int = 0
    for city in ConfigJSON['cityList']:
        print(f'Getting weather for {city} ...')
        cityData:dict = weather.GetWeatherPerCity(WM.WeatherMange.ApiCall,
                                                  ConfigJSON['apiKeyOpenWeather'],
                                                  city
                                                  )
        for attempt in range(5):
            try:
                client: object = TI.TweeterManagement.ClientAuth(ConfigJSON['bearerTokenTweeter'],
                                                             ConfigJSON['apiKeyTweeter'],ConfigJSON['apiSecretTweeter'],
                                                             ConfigJSON['accessTokenTweeter'],
                                                             ConfigJSON['accessTokenSecretTweeter']
                                                             )
                tweetBody = TI.TweeterManagement.PrepareTweet(cityData)
                #print(tweetBody)
                TI.TweeterManagement.CreateTweet(client,tweetBody)
                counter+=1
            except SystemError as e:
                print(f'Error happend -> {e} ...')
            else:
                break
        else:
            print('Cannot connect to twitter after 10 tries...')


    print(f'Job done, tweet posted -> {counter} ...')

if __name__ == '__main__':
    main()