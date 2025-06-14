# weather_plugin.py
import requests

def get_weather(city="chittoor"):
    api_key = "pyRrPeDrmiftYamsze7Fwf1NLitWwlng"  # Replace with your actual Tomorrow.io API key
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['data']['values']['temperature']
        desc = data['data']['values'].get('weatherCode', 'Unknown')
        return f"The weather in {city} is {desc} with {temp}°C."
    else:
        return "Sorry, I couldn't fetch the weather right now."

def run():
    print(get_weather("chittoor"))
