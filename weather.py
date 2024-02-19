# Import necessary libraries
from dotenv import load_dotenv  # To load environment variables from .env file
from pprint import pprint  # To pretty-print data structures
import requests  # To make HTTP requests
import os  # To access environment variables

# Load environment variables from a .env file located in the same directory as this script.
load_dotenv()

def get_current_weather(city="Washington DC"):
    """
    Fetches the current weather conditions for a specified city using the OpenWeatherMap API.

    Parameters:
    - city (str): The name of the city for which to retrieve weather data. Default is "Washington DC".

    Returns:
    - dict: A dictionary containing the current weather data retrieved from the OpenWeatherMap API.
    """
    # Construct the request URL with the API key and city name, using imperial units for temperature (Fahrenheit).
    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"
    
    # Make a GET request to the OpenWeatherMap API and parse the response as JSON.
    weather_data = requests.get(request_url).json()
    
    # Return the parsed JSON data.
    return weather_data

# This block is executed if the script is run directly (not imported as a module).
if __name__ == "__main__":
    # Display a welcome message.
    print("\n*** Get Current Weather Conditions ***\n")
    
    # Prompt the user to enter a city name.
    city = input("\nPlease enter a city: ")
    
    # If the user input is empty or only contains whitespace, default to "Washington, DC".
    if not bool(city.strip()):
        city = "Washington, DC"
    
    # Fetch the current weather for the specified city.
    weather = get_current_weather(city)
    
    # Pretty-print the weather data.
    print("\n")
    pprint(weather)