#!/usr/bin/env python3
"""Fetch Tokyo weather and save to file."""

import urllib.request
import json
from datetime import datetime

def get_tokyo_weather():
    """Fetch current weather in Tokyo using Open-Meteo API (no API key needed)."""
    # Tokyo coordinates
    url = "https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&current_weather=true&timezone=Asia/Tokyo"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        return {"error": str(e)}

def format_weather(data):
    """Format weather data as readable text."""
    if "error" in data:
        return f"Error fetching weather: {data['error']}"

    current = data.get("current_weather", {})
    temp = current.get("temperature", "N/A")
    windspeed = current.get("windspeed", "N/A")
    weather_code = current.get("weathercode", 0)

    # Simple weather code mapping
    weather_types = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Foggy", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
        95: "Thunderstorm"
    }
    condition = weather_types.get(weather_code, f"Unknown ({weather_code})")

    output = f"""Tokyo Weather Report
====================
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Temperature: {temp}°C
Wind Speed: {windspeed} km/h
Condition: {condition}
"""
    return output

def main():
    # Fetch weather
    weather_data = get_tokyo_weather()

    # Format and display
    weather_text = format_weather(weather_data)
    print(weather_text)

    # Save to file
    filename = "tokyo_weather_report.txt"
    with open(filename, "w") as f:
        f.write(weather_text)

    print(f"Weather report saved to {filename}")

if __name__ == "__main__":
    main()
