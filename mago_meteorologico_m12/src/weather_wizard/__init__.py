"""
Este archivo expone las funciones principales para que sean fáciles de importar.
"""

from .engine import get_weather_data
from .api import fetch_weather_from_provider

# Esto define qué se importa cuando alguien hace "from weather_wizard import *"
__all__ = ["get_weather_data", "fetch_weather_from_provider"]

__version__ = "0.1.0"
__author__ = "Tu Nombre o el de tus Estudiantes"