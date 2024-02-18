from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        country = data["sys"]["country"]

        return {
            "city": city,
            "country": country,
            "description": weather_description,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed
        }
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    api_key = "YOUR_API_KEY_HERE"  # Replace this with your own OpenWeatherMap API key

    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_weather(api_key, city)
        if weather_data:
            return render_template("index.html", weather_data=weather_data)
        else:
            error_message = "City not found. Please enter a valid city name."
            return render_template("index.html", error_message=error_message)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
