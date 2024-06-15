#Twitter(x) integration to post tweets
import tweepy

class TweeterManagement():
    @staticmethod
    def ClientAuth(bearerToken: str,apiKey: str,apiSecret: str,accessToken: str,accessTokenSecret: str)-> object:
        try:
            print('Conecting to tweeter...')
            client = tweepy.Client(bearerToken,apiKey,apiSecret,accessToken,accessTokenSecret)
            print('Connection established...')
            return client
        except:
            print('Error while authenticating...')

    @def convertToCelcius(temp: float):
    @staticmethod
    def PrepareTweet(cityWeather: dict)->str:
        tweetBody = '''\
                Miasto: {city}
                Pogoda: {weather}
                Temp. minimalna: {tempMin}
                Temp. maksymalna: {tempMax}
                Zachmurzenie: {humidity}%\
                '''.format(city=cityWeather['cityName'],
                               weather=cityWeather['weather'],
                               tempMin=cityWeather['tempMin'],
                               tempMax=cityWeather['tempMax'],
                               humidity=cityWeather['humidity']
                               )


        return  tweetBody

    @staticmethod
    def CreateTweet(client:object,tweetBody: str)->None:
        client.create_tweet(text=tweetBody)