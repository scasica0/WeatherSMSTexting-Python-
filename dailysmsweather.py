

import yweather
import sys
from twilio.rest import TwilioRestClient
import time

#Returns weather report from yahoo weather
def weatherReport(city):
    client = yweather.Client( )
    woeid = client.fetch_woeid(city)
    weather = client.fetch_weather(woeid, metric=False)

    location ='{},{}'.format(weather['location']['city'], weather['location']['region'])

    todaysforecast = weather['forecast'][0]

    forecast = 'Location: {} \nDate:  {} \nHigh: {}ºF \nLow: {}ºF \nCloud Coverage: {}'.format(location, todaysforecast['date'], todaysforecast['high'], todaysforecast['low'], todaysforecast['text'])

    return forecast

#Sends sms messsage containing text to inputed number using Twilio
def sendTextMessage(text, number):
    # My Account Sid and Auth Token
    ACCOUNT_SID = "ACbc2ba2f0dcfa7da8056a89f81340cef5" 
    AUTH_TOKEN = "7609ef3decd0d65b73b1c5350eb8f127"
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(body=text,
    to="+" + number, # Phone number to send to
    from_="+19494461307") # My Twilio number

#Sets program to run everyday at x hour and y minutes (24-hour format)
def dailySleep(x, y):
    end_time = (time.localtime().tm_hour*60*60 + time.localtime().tm_min * 60 + time.localtime().tm_sec)
    send_time = (x*60*60 + y*60)        
    start_time = (24*60*60 - (end_time - send_time)) 
    time.sleep(start_time)


def main():
    dailySleep(8, 0) #waits until time specified (8:00) to run program
    while True: #infinite loop
        forecast = weatherReport(sys.argv[1])
        sendTextMessage(forecast, sys.argv[2])
        dailySleep (8, 0) #runs program everyday at time specified (8:00)

if __name__== "__main__":
    main()






