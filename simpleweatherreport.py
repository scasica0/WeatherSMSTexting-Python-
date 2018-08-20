

import yweather
import sys

#Returns weather report from yahoo weather
def weatherReport(city):
    client = yweather.Client( )
    woeid = client.fetch_woeid(city)
    weather = client.fetch_weather(woeid, metric=False)

    location ='{},{}'.format(weather['location']['city'], weather['location']['region'])

    todaysforecast = weather['forecast'][0]

    forecast = 'Location: {} \nDate:  {} \nHigh: {}ºF \nLow: {}ºF \nCloud Coverage: {}'.format(location, todaysforecast['date'], todaysforecast['high'], todaysforecast['low'], todaysforecast['text'])

    return forecast

def main():
    print (weatherReport(sys.argv[1]))

if __name__== "__main__":
    main()
