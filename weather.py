from dotenv import load_dotenv
import requests
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city="Washington DC"):
    """
    Retrieves current weather conditions for the specified city from the OpenWeatherMap API.

    Args:
    - city (str): City name for which weather data is to be fetched. Defaults to "Washington DC".

    Returns:
    - dict: Weather data for the specified city.
    """
    api_key = os.getenv('API_KEY')
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'appid': api_key,
        'q': city,
        'units': 'imperial'  # Use imperial units (Fahrenheit) for temperature
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    return weather_data

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city_input = input("Please enter a city: ").strip()

    city = city_input if city_input else "Washington, DC"
    weather = get_current_weather(city)

    print("\nWeather data for", city, ":\n")
    pprint(weather)
