import requests
import datetime

api_path = 'C:/Users/JakeLaptop/Documents/GitHub/LiveWeather_Arduino/API_KEY.txt'
with open(api_path, "r") as file: api_token = file.read()
api_address = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/351409?apikey='+ api_token + '&language=en-us&details=false&metric=false'
api_address_curr = 'http://dataservice.accuweather.com/currentconditions/v1/351409?apikey=' + api_token + '%20&language=en-us&details=false'
r = requests.get(api_address)

def Phrase(hour):
    if hour == 0:
        f = requests.get(api_address_curr)
        for key, value in f.json()[0].items():
            if key == 'WeatherText':
                time = datetime.datetime.now().hour
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


for i in range(0,11):
    Phrase(i)

