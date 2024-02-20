from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    """Renders the homepage."""
    return render_template('index.html')

@app.route('/popular')
def popular():
    """Renders the page with popular cities."""
    return render_template('popular.html')

@app.route('/weather')
def get_weather():
    """
    Fetches and displays weather information for a specified city.
    
    Retrieves city from query parameters, defaults to "Washington DC" if not specified or invalid.
    On successful weather data retrieval, renders the weather page with detailed weather information.
    If the city is not found, renders a city-not-found error page.
    """
    city = request.args.get("city", "Washington DC").strip()
    weather_data = get_current_weather(city)
    
    if weather_data["cod"] != 200:
        return render_template('city-not-found.html')
    
    main_weather_descrip = weather_data['weather'][0]['main'].lower()
    
    # Using dictionaries instead of if-elifs for efficiency and maintainability
    # Map weather conditions to specific video and image files
    weather_to_video = {
        "clear": 'clear.mp4',
        "clouds": 'clouds.mp4',
        "rain": 'rain.mp4',
        "drizzle": 'rain.mp4',
        "thunderstorm": 'rain.mp4',
        "snow": 'snow.mp4',
        "fog": 'fog.mp4',
        "smoke": 'fog.mp4',
        "mist": 'fog.mp4'
    }
    
    weather_to_img = {
        "clouds": 'clouds.png',
        "rain": 'rain.png',
        "drizzle": 'rain.png',
        "thunderstorm": 'rain.png',
        "snow": 'snow.png',
        "fog": 'fog.png',
        "smoke": 'fog.png',
        "mist": 'fog.png'
    }
    
    status_video = weather_to_video.get(main_weather_descrip, 'intro.mp4')
    status_img = weather_to_img.get(main_weather_descrip, 'logo.png')
    
    return render_template(
        "weather.html", back_video=status_video, status_image=status_img,
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        humidity=weather_data["main"]["humidity"],
        wind_speed=f"{weather_data['wind']['speed']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
