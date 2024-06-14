import WeatherManagment as WM

def main():
    weather: object = WM.WeatherMange()
    ConfigJSON: dict = weather.GetDataFromJson()
    print(ConfigJSON)
    weather.CheckApi(ConfigJSON['apiKey'])

    for city in ConfigJSON['cityList']:
        weather.GetWeatherPerCity(WM.WeatherMange.ApiCall, ConfigJSON['apiKey'], city)


if __name__ == '__main__':
    main()