"""
Code developed independently of Arduino C++ code.
Uses the Accuweather API to display current weather in Seattle, WA for next 12 hours.

This will be used to display hourly weather on a LED strip with colors relating to weather conditions. 
"""

#Current Bugs: Time between 9AM and 12PM and being subtracted by 12.

import time
import requests
import datetime

current_w_path = 'C:/Users/JakeLaptop/Documents/GitHub/LiveWeather_Arduino/Current_Weather_API_Address.txt'
future_w_path = 'C:/Users/JakeLaptop/Documents/GitHub/LiveWeather_Arduino/Future_Weather_API_Address.txt'
with open(current_w_path, "r") as file: api_address_curr = file.read()
with open(future_w_path, "r") as file: api_address = file.read()

#A separate API function is used for current and future weather conditions, api_address_curr, recieves current weather.
r = requests.get(api_address)
f = requests.get(api_address_curr)

#For future work of outputting data in csv file or other file to be read into Arduino code
output_weather = []
output_time = []
output_dict = [dict() for x in range(0,11)]

#For Dev. code
current_hour = 0

"""
Code currently in development
"""
def Weather_Update():
    for i in range(0,12):
        #Current Hour Weather
        if i == 0:
            for key, value in f.json()[0].items():
                if key == "WeatherText":
                    AMPM(current_hour)
                    output_weather.append(value) 
        #Future Hour Weather
        else:
            for key, value in r.json()[i-1].items():
                if key == "IconPhrase":
                    future_hour = datetime.datetime.now().hour + i
                    AMPM(future_hour)
                    output_weather.append(value)


def AMPM(time):
    print(str(time))
    if time > 24:
        time = time - 24
        ampm = "AM"
    elif time > 12 & time < 24:
        print('elif')
        time = time - 12
        ampm = "PM"
        if time == 12:
            ampm = "AM"
    else:
        ampm = datetime.datetime.now().strftime("%p")
    output_time.append(str(time) + ampm) 


while True:
    time.sleep(5)
    if datetime.datetime.now().hour != current_hour:
        current_hour = datetime.datetime.now().hour
        Weather_Update()
        print(str(output_weather))
        print(str(output_time))
    else:
        pass


