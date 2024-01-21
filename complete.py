# https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACd400b5d0d939acbe909d1994f646d91a"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+13614704092",
        to="+61413876131"
    )
    print(message.status)




OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
import requests
api_key = "a8c0ed87002f7ebdfa144794ae520fb8"

weather_param = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

response = requests.get(url=OWN_Endpoint, params=weather_param)
print(response.status_code)
Weather_data = response.json()
print(Weather_data)
print(Weather_data['weather'])





