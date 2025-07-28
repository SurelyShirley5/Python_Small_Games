import requests, smtplib

my_email = "your email"
to_email = "the email to send to"
password = "your password"

API = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "your api key"
TAIPEI_LAT = 25.032969
TAIPEI_LON = 121.565414

parameters = {
    "lat": TAIPEI_LAT,
    "lon": TAIPEI_LON,
    "appid": API_KEY, # Key Name for API Key: appid
    "cnt": 4,
}

response = requests.get(url=API, params=parameters)
response.raise_for_status()
forecast_data = response.json()['list']

forecast_hour_weathers = [forecast['weather'][0]['id'] for forecast in forecast_data]

for i in forecast_hour_weathers:
    if i < 700:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg="Subject:Gonna Rain, Bring an Umbrella!\n\n"
            )
        break
