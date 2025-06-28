import requests
import json

city = "London" 

# Load config
with open("weather_apikey.config", "r") as f:
    config = json.load(f)
    print(config)

API_KEY = config['openweather']['api_key']
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    sea_level = data['main'].get('sea_level', 'N/A')
    grnd_level = data['main'].get('grnd_level', 'N/A')
    country = data['sys'].get('country', 'N/A')
    weather_desc = data['weather'][0].get('description', 'N/A')

    print(f"🌊 Sea Level: {sea_level} hPa")
    print(f"🏔️ Ground Level: {grnd_level} hPa")
    print(f"🏳️ Country: {country}")
    print(f"🌤️ Weather: {weather_desc}")
else:
    print("Failed to get data:", response.status_code)
    print("Response Body:", response.json())