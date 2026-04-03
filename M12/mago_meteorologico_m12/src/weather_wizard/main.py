"""
Punto de entrada para la aplicación Weather Wizard.
Este archivo coordina la interfaz de usuario con el motor de lógica.
"""
from weather_wizard.motor import obtener_clima_ciudad

ciudad = input("Introduce una ciudad: ")
resultado = obtener_clima_ciudad(ciudad)

if "error" in resultado:
    print("Error:", resultado["error"])
else:
    print("\nClima actual:")
    print(f"Ciudad: {resultado['city']}")
    print(f"Temperatura: {resultado['temp']}°C")
    print(f"Condición: {resultado['condition']}")
        
        # 3. Procesamiento/Formateo
        mensaje_final = formatear_respuesta(datos_crudos)
        
        # 4. Salida
        print(f"\nResultado: {mensaje_final}")
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
