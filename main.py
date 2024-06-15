import WeatherManagment as WM
import TwitterIntegration as TI
import General

def main():
    weather: object = WM.WeatherMange()
    ConfigJSON: dict = General.General.GetDataFromJson()
    #print(ConfigJSON)
    weather.CheckApi(ConfigJSON['apiKeyOpenWeather'])

    for city in ConfigJSON['cityList']:
        cityData:dict = weather.GetWeatherPerCity(WM.WeatherMange.ApiCall, ConfigJSON['apiKeyOpenWeather'], city)
        client: object = TI.TweeterManagement.ClientAuth(ConfigJSON['bearerTokenTweeter'],ConfigJSON['apiKeyTweeter'],ConfigJSON['apiSecretTweeter'],ConfigJSON['accessTokenTweeter'],ConfigJSON['accessTokenSecretTweeter'])
        tweetBody = TI.TweeterManagement.PrepareTweet(cityData)
        TI.TweeterManagement.CreateTweet(client,tweetBody)

if __name__ == '__main__':
    main()