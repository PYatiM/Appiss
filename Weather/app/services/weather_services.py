import requests
from flask import current_app

def get_weather(city):
    api_key = current_app.config["OPENWEATHER_API_KEY"]
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "success": True,
            "city": data["name"],
            "temp": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"]
        }

    except requests.exceptions.RequestException:
        return {"success": False, "error": "City not found or API error"}
