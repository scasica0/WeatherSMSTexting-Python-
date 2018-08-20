

import yweather
import sys
from twilio.rest import TwilioRestClient
import time

#Returns sunset time (in seconds) from yahoo weather (24 hour format)
def sunsetReport(city):
    client = yweather.Client( )
    woeid = client.fetch_woeid(city)
    weather = client.fetch_weather(woeid, metric=False)

    sunset = weather["astronomy"]["sunset"]
    
    #adjust for 24-hour format in chance that sunset is in during 'am' hours
    if sunset[5:7] == 'pm': 
        hour = (int(sunset[0:1]) + 12)
        minute = int(sunset[2:4])
    else:      
        hour = int(sunset[0:1])
        minute = int(sunset[2:4])

    return (hour, minute)

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
    #set variables for hour and minute of sunset
    (sunset_hour,sunset_minute) = sunsetReport(sys.argv[1])
    sunset_hour *= 60*60
    sunset_minute = (sunset_minute-5)*60 #adjust for 5 minutes before sunset

    dailySleep(sunset_hour, sunset_minute) #waits until specified hour and minute to run program
    while True: #infinite loop (runs program everyday at specified hour and minute)
        (sunset_hour,sunset_minute) = sunsetReport(sys.argv[1])
        sunset_hour *= 60*60
        sunset_minute = (sunset_minute-5)*60
        sendTextMessage("Sunset is in 5 Minutes.", sys.argv[2])
        dailySleep(sunset_hour, sunset_minute)  

if __name__== "__main__":
    main()






