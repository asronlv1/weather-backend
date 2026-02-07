# Weather App – Phase 1

This project includes two parts:
- Backend service for fetching weather data
- Frontend dashboard for displaying the data

Running locally means running the application directly on your machine using Python, without Docker.

Backend
---------------

Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Running locally

export OPENWEATHER_API_KEY="YOUR_API_KEY"
python app/app.py

The backend runs on:
http://127.0.0.1:5000OpenWeatherMap API key setup

Go to https://openweathermap.org/api
Sign up for a free account
Generate an API key

Set the API key as an environment variable:
export OPENWEATHER_API_KEY="YOUR_API_KEY"

API endpoint
GET /weather/<location_key>

Supported location keys:

newyork
sydney
capetown
bangkok

The endpoint returns current weather data including temperature, weather description,
and optionally humidity and wind speed.

Optional curl examples
curl http://127.0.0.1:5000/weather/newyork
curl http://127.0.0.1:5000/weather/sydney
curl http://127.0.0.1:5000/weather/capetown
curl http://127.0.0.1:5000/weather/bangkok

