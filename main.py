import requests
import json
import os
from twilio.rest import Client

# Constants update with your info
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "eec3d79173a3898efcc286db6eab7e45"
ACCOUNT_SID = "AC2ec366d5911842c63087570e609047b7"
AUTH_TOKEN = 'cb1088f9034f187cfc2251e82cca1466'
CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)

weather_params = {
    "lat": 44.052071,
    "lon": -123.086754,
    "appid": API_KEY,
    "units": "imperial",
    "exclude": "current,alerts,daily,minutely"
}

data = requests.get(OWM_ENDPOINT, params=weather_params)
hourly_data = data.json()
hourly_json = json.dumps(hourly_data, indent=4)

# sends a message if it's going to rain

def rain_today():
    message = CLIENT.messages.create(
        body="It's going to rain today. Don't forget your umbrella",
        from_='+18149294372',
        to='+13609134165'
    )


# function that checks if it will rain in next 12 hours
def check_for_rain():
    with open("hourly_data.json", "w") as file:
        file.write(hourly_json)

    with open("hourly_data.json", "r") as file:
        hour = json.load(file)
        hourly = hour["hourly"]
        unix = hourly[0]["dt"]
        for i in hourly:
            if i["dt"] <= (unix + 39600) and i["weather"][0]["id"] < 900:
                return True


if check_for_rain():
    rain_today()


