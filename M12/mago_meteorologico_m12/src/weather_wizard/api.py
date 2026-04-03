"""
Módulo para manejar las comunicaciones externas.
Este archivo se encarga de conectar con servidores de clima reales.
"""
import requests

API_KEY = "29dc97f0657f40b7b4e20326260304"

def is_valid_city_name(city_name):
    return city_name.replace(" ", "").isalpha()

def fetch_weather_from_provider(city_name):
    #  se cambia  HTTPS (no HTTP)
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}&aqi=no"

    try:
        response = requests.get(url, timeout=10)

        # Si la API responde bien
        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:
        return {"error": "❌ Sin conexión a internet o servidor bloqueado."}

    except requests.exceptions.Timeout:
        return {"error": "⏱️ La API tardó demasiado en responder."}

    except requests.exceptions.HTTPError:
        return {"error": f"⚠️ Error HTTP: {response.status_code}"}

    except Exception as e:
        return {"error": f"❌ Error inesperado: {e}"}

def obtener_clima_ciudad(city_name: str):
    if not is_valid_city_name(city_name):
        return {"error": "Nombre de ciudad no válido."}

    raw_data = fetch_weather_from_provider(city_name)

    # Si hubo error, lo devolvemos directo
    if "error" in raw_data:
        return raw_data

    return {
        "city": raw_data.get("location", {}).get("name", "N/A"),
        "temp": raw_data.get("current", {}).get("temp_c", "N/A"),
        "condition": raw_data.get("current", {}).get("condition", {}).get("text", "N/A")
    }

# 🔹 PRUEBA
if __name__ == "__main__":
    ciudad = input("Introduce una ciudad: ")

    resultado = obtener_clima_ciudad(ciudad)

    if "error" in resultado:
        print(resultado["error"])
    else:
        print("\nClima actual:")
        print(f"Ciudad: {resultado['city']}")
        print(f"Temperatura: {resultado['temp']}°C")
        print(f"Condición: {resultado['condition']}")