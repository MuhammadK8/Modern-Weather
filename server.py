# Import Flask for the web app, render_template for rendering HTML templates,
# and request for accessing request data
from flask import Flask, render_template, request
# Import the get_current_weather function from the weather module to fetch weather data
from weather import get_current_weather
# Import serve from waitress to serve the app in a production-ready server
from waitress import serve

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the root and index page
@app.route('/')
@app.route('/index')
def index():
    """
    Render the homepage of the web application.

    Returns:
        The rendered template for the index.html page.
    """
    # Render and return the index.html template
    return render_template('index.html')

# Define the route for fetching and displaying weather information
@app.route('/weather')
def get_weather():
    """
    Fetches weather data for a specified city and renders the weather information page.

    Returns:
        The rendered template for the weather page with weather data or an error page if city not found.
    """
    # Retrieve the city name from the query parameters. Default to None if not provided.
    city = request.args.get("city")
    
    # Default to "Washington DC" if no city is provided or if the input is only whitespace
    if not city or not bool(city.strip()):
        city = "Washington DC"
        
    # Fetch the current weather data for the specified city
    weather_data = get_current_weather(city)
    
    # Handle incorrect city by checking the status code in the weather data response
    if not weather_data["cod"] == 200:
        # Render and return the city-not-found.html template if the city is not found
        return render_template('city-not-found.html')
    
    # Render and return the weather.html template with weather data if the city is found
    return render_template(
                        "weather.html", 
                        title=weather_data["name"],
                        status=weather_data["weather"][0]["description"].capitalize(),
                        temp=f"{weather_data['main']['temp']:.1f}",
                        feels_like=f"{weather_data['main']['feels_like']:.1f}"
                        )

# The application entry point
if __name__ == "__main__":
    # Serve the app using Waitress on host 0.0.0.0 and port 8000
    serve(app, host='0.0.0.0', port=8000)