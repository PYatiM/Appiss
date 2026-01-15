from flask import Flask
from app.controllers.weather_controller import weather_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    app.register_blueprint(weather_bp)

    return app
