#Twitter(x) integration to post tweets
import tweepy


class TweeterManagement():
    @staticmethod
    def ClientAuth(bearerToken: str, apiKey: str, apiSecret: str, accessToken: str, accessTokenSecret: str) -> object:
        try:
            print('Conecting to tweeter...')
            client = tweepy.Client(bearerToken, apiKey, apiSecret, accessToken, accessTokenSecret)
            print('Connection established...')
            return client
        except:
            print('Error while authenticating...')

    @staticmethod
    def PrepareTweet(cityWeather: dict) -> str:
        tweetBody = ("Miasto: {city1}\nPogoda: {weather}\n"
                     "Temperatura: {tempMin} C\n"
                     "Wilgotność: {humidity}%\n"
                     "#Polska #{city} #Pogoda").format(city1=str(cityWeather['cityName']),
                                                       city=str(cityWeather['cityName']).replace(" ",""),
                                                       weather=cityWeather['weather'],
                                                       tempMin=cityWeather['tempMin'],
                                                       humidity=cityWeather['humidity']
                                                       )
        return tweetBody

    @staticmethod
    def CreateTweet(client: object, tweetBody: str) -> None:
        try:
            client.create_tweet(text=tweetBody)
            print('Tweet posted...')
        except SystemError as e:
            print('Error while posting tweet...')
            print(e)
