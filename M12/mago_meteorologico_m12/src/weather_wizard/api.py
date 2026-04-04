import requests

# Tu llave real de WeatherAPI
API_KEY = "5fb8ffc744df481897c11151260404"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

def fetch_weather_from_provider(city_name: str) -> dict:
    parametros = {
        "key": API_KEY,
        "q": city_name,
        "lang": "es"
    }
    respuesta = requests.get(BASE_URL, params=parametros, timeout=10)
    respuesta.raise_for_status() # Esto lanza error si la ciudad no existe
    return respuesta.json()