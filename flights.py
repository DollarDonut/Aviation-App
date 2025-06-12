import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_flights(iata_code):
    url = f"https://aerodatabox.p.rapidapi.com/flights/airports/iata/{iata_code}"

    querystring = {
        "direction": "Both",
        "withLeg": "true",
        "withCancelled": "false",
        "withCodeshared": "true",
        "withCargo": "false",
        "withPrivate": "false",
        "withLocation": "false",
        "offsetMinutes": "-60",
        "durationMinutes": "360"
    }

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print("API error:", response.status_code, response.text)
        return None
