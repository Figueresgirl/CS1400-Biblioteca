"""
Punto de entrada para la aplicación Weather Wizard.
"""

from weather_wizard.motor import obtener_clima_ciudad


def main():
    try:
        ciudad = input("Introduce una ciudad: ")
        resultado = obtener_clima_ciudad(ciudad)

        if "error" in resultado:
            print("Error:", resultado["error"])
        else:
            print("\nClima actual:")
            print(f"Ciudad: {resultado['city']}")
            print(f"Temperatura: {resultado['temp']}°C")
            print(f"Condición: {resultado['condition']}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()