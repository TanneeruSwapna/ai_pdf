from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Streamlit to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "289f0192ca3981e90c537848411e4b39"

class WeatherRequest(BaseModel):
    city: str

@app.post("/weather")
def get_weather(data: WeatherRequest):

    city = data.city

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        return {"answer": "City not found"}

    weather_data = response.json()

    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    if "rain" in description.lower():
        advice = "There is a chance of rain. Carry an umbrella."
    elif temp > 35:
        advice = "Very hot weather. Stay hydrated."
    else:
        advice = "Weather looks good. You can go outside."

    answer = f"""
City: {city}

Temperature: {temp}°C

Humidity: {humidity}%

Condition: {description}

Advice: {advice}
"""

    return {"answer": answer}