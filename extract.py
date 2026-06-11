import requests
import os
from dotenv import load_dotenv

load_dotenv()

def extract_weather():

    CITY = os.getenv("CITY")
    API_KEY = os.getenv("API_KEY")

    if not CITY or not API_KEY:
        raise ValueError("Missing CITY or API_KEY")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    print("Modified by Wajd")

    return data

  
