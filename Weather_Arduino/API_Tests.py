"""
Code developed independently of Arduino C++ code.
Uses the Accuweather API to display current weather in Seattle, WA for next 12 hours.

This will be used to display hourly weather on a LED strip with colors relating to weather conditions. 
"""

import requests
import datetime

current_w_path = 'C:/Users/JakeLaptop/Documents/GitHub/LiveWeather_Arduino/Current_Weather_API_Address.txt'
future_w_path = 'C:/Users/JakeLaptop/Documents/GitHub/LiveWeather_Arduino/Future_Weather_API_Address.txt'
with open(current_w_path, "r") as file: api_address_curr = file.read()
with open(future_w_path, "r") as file: api_address = file.read()

#A separate API function is used for current and future weather conditions, api_address_curr, recieves current weather.
r = requests.get(api_address)
f = requests.get(api_address_curr)

#Will more than likely separate in the future to create multiple functions.
def Phrase(hour):
    """
    Based on the hour being evaluated, time and conditions are found and displayed
    """
    if hour == 0:
        #Necessary for current weather since Accuweather's API has two separate functions for current vs. future
        for key, value in f.json()[0].items():
            if key == 'WeatherText':
                time = datetime.datetime.now().hour
                #Requires simplification, this is just the current way to get datetime to properly output adjusted hours.
                if time > 24:
                    time = time - 24
                    ampm = "AM"
                elif time > 12 & time < 24:
                    time = time - 12
                    ampm = "PM"
                    if time == 12:
                        ampm = "AM"
                else:
                    ampm = datetime.datetime.now().strftime("%p")

                print("Weather at " + str(time) +""+ ampm + " is " + value)
    #For all other instances besides current weather
    else:
        for key, value in r.json()[hour - 1].items():
            if key == 'IconPhrase':
                time = datetime.datetime.now().hour + i
                if time > 24:
                    time = time - 24
                    ampm = "AM"
                elif time > 12 & time < 24:
                    time = time - 12
                    ampm = "PM"
                    if time == 12:
                        ampm = "AM"
                else:
                    ampm = datetime.datetime.now().strftime("%p")

                print("Weather at " + str(time) + ampm+ "" + " is " + value)

#Used to only evaluate current and future 11 hours, since free API access is only allowed 12 hours in total. 
for i in range(0,11):
    Phrase(i)

