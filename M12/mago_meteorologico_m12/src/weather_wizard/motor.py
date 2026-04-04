from weather_wizard.api import fetch_weather_from_provider

def obtener_clima_ciudad(nombre_ciudad):
    try:
        # Llamamos a la API que ya tiene tu llave
        datos = fetch_weather_from_provider(nombre_ciudad)
        
        # Extraemos solo lo que el Main necesita mostrar
        return {
            "city": datos["location"]["name"],
            "temp": datos["current"]["temp_c"],
            "condition": datos["current"]["condition"]["text"]
        }
    except Exception as e:
        # Si algo falla, mandamos el error de vuelta
        return {"error": str(e)}