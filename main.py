import requests
import json
import os
from twilio.rest import Client

# Constants update with your info
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "**YOUR OPEN WEATHER API KEY**"
ACCOUNT_SID = "**TWILIO SID**"
AUTH_TOKEN = '**TWILIO AUTH TOKEN**'
CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)

weather_params = {
    "lat": **YOUR LAT**,
    "lon": **YOUR LONG**,
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
        from_='**TWILIO NUMBER**',
        to='**NUMBER YOU WANT TO SEND TO**'
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


