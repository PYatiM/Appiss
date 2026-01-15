from flask import Blueprint, render_template, request
from app.services.weather_services import get_weather

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if city:
            result = get_weather(city)
            if result["success"]:
                weather = result
            else:
                error = result["error"]
        else:
            error = "Please enter a city name"

    return render_template("index.html", weather=weather, error=error)
