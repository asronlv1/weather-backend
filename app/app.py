import os
import requests
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

LOCATIONS = {
    "newyork": "New York",
    "sydney": "Sydney",
    "capetown": "Cape Town",
    "bangkok": "Bangkok",
}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/weather/<location_key>")
def weather(location_key: str):
    if not API_KEY:
        return jsonify(error="Missing OPENWEATHER_API_KEY"), 500

    key = location_key.lower().strip()
    if key not in LOCATIONS:
        return jsonify(error="Invalid location_key", allowed=list(LOCATIONS.keys())), 400

    city = LOCATIONS[key]

    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": API_KEY, "units": "metric"},
        timeout=10,
    )

    if r.status_code != 200:
        return jsonify(error="OpenWeather error", details=r.json()), r.status_code

    data = r.json()

    return jsonify({
        "location_key": key,
        "city": data.get("name", city),
        "temperature_c": data["main"]["temp"],
        "description": data["weather"][0]["description"] if data.get("weather") else None,
        "humidity": data["main"].get("humidity"),
        "wind_speed": data.get("wind", {}).get("speed"),
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
