# 🌦️ Weather Web Application (Flask MVC)

A production-ready weather web application built using **Flask**, following a clean **MVC architecture**, styled with **Bootstrap**, and powered by the **OpenWeather API**.

---

## 🚀 Features
- Search weather by city name
- Real-time temperature & conditions
- Clean MVC separation
- Responsive Bootstrap UI
- Production deployment ready

---

## 🏗️ Architecture (MVC)

- **Model / Service**: API interaction & business logic
- **View**: Jinja2 templates with Bootstrap
- **Controller**: Flask Blueprints for routing

---

## 📁 Project Structure

weather-app/
├── app/
│ ├── controllers/
│ ├── services/
│ ├── templates/
│ └── static/
├── config.py
├── run.py
├── requirements.txt
└── Procfile


---

## 🔑 Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/weather-app.git
cd weather-app

### 2. Create virtual environment

python -m venv venv
source venv/bin/activate

### 3.Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

OPENWEATHER_API_KEY=your_api_key_here

### 5. Run locally

python run.py



## Project working and content usage

### 1. __init__.py - App Factory

What it does

Creates and configures the Flask application

Why it exists

Follows Flask’s application factory pattern

Allows multiple configurations (dev, test, prod)

Makes the app scalable and testable

How it’s implemented
from flask import Flask
from app.controllers.weather_controller import weather_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    app.register_blueprint(weather_bp)
    return app

How it works

Initializes Flask

Loads environment-based configuration

Registers controllers (routes)

Returns a ready-to-run app instance

### 2. run.py - Application Entry Point

What it does

This is the main entry file used to start the application.

Gunicorn and Flask both look for the app object here.

Why it exists

Keeps application startup separate from configuration

Enables production deployment

How it’s implemented
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

How it works

Imports the Flask app factory

Creates an application instance

Starts the development server when run directly

In production, Gunicorn runs app from here


## 3. config.py — Configuration Layer

What it does

Stores application configuration

Loads sensitive data safely

Why it exists

Avoids hardcoding secrets

Centralizes config management

How it’s implemented
import os

class Config:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

How it works

Reads API key from environment variables

Makes config accessible to all app components


### 4. weather_controller.py — Controller Layer

What it does

Handles HTTP requests and responses

Acts as the decision-maker of the app

Why it exists

Keeps routing logic separate from business logic

Improves readability and maintainability

How it’s implemented
from flask import Blueprint, render_template, request
from app.services.weather_service import get_weather

Key Responsibilities

Receives city input from the user

Calls the weather service

Passes data to the view (HTML template)

How it works

User submits city name via form

Controller receives POST request

Calls get_weather(city)

Decides success or error

Renders HTML with result


### 5. weather_service.py — Model / Service Layer

What it does

Communicates with the OpenWeather API

Processes and returns weather data

Why it exists

Separates business logic from routing

Makes API logic reusable

How it’s implemented
import requests
from flask import current_app

Key Responsibilities

Builds API request

Handles errors

Normalizes API response

How it works

Reads API key from app config

Sends HTTP request to OpenWeather

Parses JSON response

Extracts relevant fields

Returns structured data to controller


### 6. index.html — View Layer

What it does

Displays the user interface

Renders weather data dynamically

Why it exists

Separates presentation from logic

Uses Jinja2 templating

How it’s implemented
{% if weather %}
    <h3>{{ weather.city }}</h3>
{% endif %}

How it works

Receives data from controller

Uses Jinja conditionals

Displays weather info or errors

Styled using Bootstrap


### 7. Static/ - Hold Static Assests(CSS)

What it does

Holds static files (CSS, images, JS)

Why it exists

Keeps styling separate from HTML

Allows future UI enhancements

Example
body {
    background-color: #f8f9fa;
}


### 8. .env — Environment Variables

What it does

Stores sensitive keys securely

Why it exists

Prevents API key leakage

Keeps secrets out of GitHub

How it works
OPENWEATHER_API_KEY=your_api_key_here


Loaded automatically via python-dotenv.


### 10. Procfile — Production Deployment

What it does

Tells hosting platforms how to run the app

Why it exists

Required for Render / Railway / Heroku

How it works
web: gunicorn run:app


<!-- flask
requests
gunicorn
python-dotenv -->
