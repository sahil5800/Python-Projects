import requests
from twilio.rest import Client


api_key = "df5c535282b5fe25c5ff503d678a5e68"
account_sid = "ACe9b109f98406bcc5dcead9d9632d12f9"
auth_token = 'e1e73555514299dcf057df59178f872d'

parameters = {
    "lat": """your latitude""",
    "lon": """your longittude""",
    "appid": api_key,
}

responce = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
responce.raise_for_status()
data = responce.json()
hourly_data = data["hourly"][:12]
id_list = []
for items in hourly_data:
    id_list.append(items["weather"][0]["id"])

will_rain = False

for elements in id_list:
    if elements < 700:
        will_rain = True

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages \
        .create(body="Hey Pluviophile, Its gonna rain today.🌧️🌧️🌧️", from_='+14159385887', to="""your number""")

    print(message.status)
else:
    message = client.messages \
        .create(body="have a nice day hope u have a get to fuck today.", from_='+14159385887', to="""your number""")

    print(message.status)
