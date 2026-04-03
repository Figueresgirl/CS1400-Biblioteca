import requests
import os
import os

API_KEY = os.getenv("API_KEY")


# Obtener API KEY desde .env
API_KEY = os.getenv("API_KEY")


# Validación
def is_valid_city_name(city_name):
    return city_name.replace(" ", "").isalpha()


# Llamada a API
def fetch_weather_from_provider(city_name):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}&aqi=no"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# Función principal
def obtener_clima_ciudad(city_name: str):
    if not is_valid_city_name(city_name):
        return {"error": "Nombre de ciudad no válido."}

    raw_data = fetch_weather_from_provider(city_name)

    if "error" in raw_data:
        return raw_data

    return {
        "city": raw_data.get("location", {}).get("name", "N/A"),
        "temp": raw_data.get("current", {}).get("temp_c", "N/A"),
        "condition": raw_data.get("current", {}).get("condition", {}).get("text", "N/A")
    }

    # Si hubo error, lo devolvemos
    if "error" in raw_data:
        return raw_data

    return {
        "city": raw_data.get("location", {}).get("name", "N/A"),
        "temp": raw_data.get("current", {}).get("temp_c", "N/A"),
        "condition": raw_data.get("current", {}).get("condition", {}).get("text", "N/A")
    }

# Prueba
if __name__ == "__main__":
    ciudad = input("Introduce una ciudad: ")
    resultado = obtener_clima_ciudad(ciudad)

    if "error" in resultado:
        print("Error:", resultado["error"])
    else:
        print("\nClima actual:")
        print(f"Ciudad: {resultado['city']}")
        print(f"Temperatura: {resultado['temp']}°C")
        print(f"Condición: {resultado['condition']}")