
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"d:\1StepGrow DS Course\Assignment\weather_sql_project\supp.env")

api_key ="8e3954cd882b7bec03374371adb91088"
base_url = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"   
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["main"],
            "description": data["weather"][0]["description"]
        }
    else:
        print(f"Error fetching {city}: {response.status_code}")
        return None

