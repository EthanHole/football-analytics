import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_URL = "https://api.football-data.org/v4"
API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")


def get_competitions():
    """Récupère la liste des compétitions accessibles."""
    headers = {
        "X-Auth-Token": API_KEY
    }

    response = requests.get(
        f"{API_URL}/competitions",
        headers=headers
    )

    response.raise_for_status()

    return response.json()

def get_standings(competition_code):
    """Récupère le classement d'une compétition."""
    headers = {
        "X-Auth-Token": API_KEY
    }

    response = requests.get(
        f"{API_URL}/competitions/{competition_code}/standings",
        headers=headers
    )

    response.raise_for_status()

    return response.json()

def get_matches(competition_code):
    """Récupère les matchs d'une compétition."""
    headers = {
        "X-Auth-Token": API_KEY
    }

    response = requests.get(
        f"{API_URL}/competitions/{competition_code}/matches",
        headers=headers
    )

    response.raise_for_status()

    return response.json()