#Twitter(x) integration to post tweets
import tweepy


class TwitterManagement():

    @staticmethod
    def client_auth(bearerToken: str, apiKey: str, apiSecret: str, accessToken: str, accessTokenSecret: str) -> object:
        """Twitter authentication"""
        for_counter = 0
        for x in range(5):
            try:
                print('Connecting to tweeter...')
                client = tweepy.Client(bearerToken, apiKey, apiSecret, accessToken, accessTokenSecret)

                if client == tweepy.errors.Unauthorized:
                    for_counter += 1
                    raise tweepy.errors.Unauthorized
                elif client == tweepy.errors.Forbidden:
                    for_counter += 1
                    raise tweepy.errors.Forbidden
                else:
                    print('Connection established....')
                    return client

            except tweepy.errors.Unauthorized as e:
                print(f'Error while authenticating, trying {for_counter}, error {e}...')
                if for_counter == 5:
                    break
            except tweepy.errors.Forbidden as e:
                if for_counter == 5:
                    break

    @staticmethod
    async def prepare_twitter(city_data: dict, *,config_json:dict) -> str:
        """Prepare post for twitter"""
        twitter_body = config_json['twitter_template'].format(city_name=city_data['city_name'],
                                                       weather_dsc=city_data['weather_dsc'],
                                                       temp_act=city_data['temp_act'],
                                                       humidity=city_data['humidity'],
                                                       pressure=city_data['pressure'],
                                                       city=city_data['city_name']
                                                       )
        return twitter_body

    @staticmethod
    async def create_twitter(*,client: object, twitter_body: str) -> None:
        """Post to twitter"""
        try:
            client.twitter(text=twitter_body)
            print('Twitter posted...')
        except tweepy.errors.BadRequest as e:
            print(f'Error while posting tweet -> \n {twitter_body}\n {e.response.status_code}...')
        except tweepy.errors.TooManyRequests as e:
            print(f'Error while posting tweet -> \n {twitter_body}\n {e.response.status_code}...')
