# ==========================================
# TAREA 1 - Introducción a Turtle 🐢
# ==========================================
# En esta actividad aprenderás a:
# 1. Mover la tortuga hacia adelante.
# 2. Girarla usando grados.
# 3. Dibujar un cuadrado.
# 4. Usar un bucle para repetir instrucciones.
#
# IMPORTANTE:
# - Un giro completo es de 360 grados.
# - Un cuadrado tiene 4 lados iguales.
# - Cada esquina de un cuadrado mide 90 grados.
#
# Completa todos los TODO.

# ------------------------------------------
# Importaciones necesarias
# ------------------------------------------

import turtle

# ------------------------------------------
# Paso 1: Crear la ventana y la tortuga
# ------------------------------------------

# TODO:
# Crea la tortuga usando make_turtle().
#No se puede utilizar make_turtle() porque no esta definida.
# La ventana debe tener 400 de alto y 400 de ancho.
#usare screen que crea la ventana grafica
#la variable se guardara en la variable ventana

# Escribe aquí tu código
#comienza por t, que es la variable que guarda las dimensiones del cuadrado
#el setup es lo que hace la variable ventana

ventana = turtle.Screen()
ventana.setup(width=400, height=400)
t = turtle. Turtle()

# ------------------------------------------
# Paso 2: Dibujar una línea
# ------------------------------------------

# TODO:
# Mueve la tortuga hacia adelante 100 pasos.
# Observa qué sucede.

# Escribe aquí tu código

t.forward(100)

# ------------------------------------------
# Paso 3: Girar la tortuga
# ------------------------------------------

# TODO:
# Gira la tortuga 90 grados hacia la izquierda.
# Luego avanza otros 100 pasos.

# Escribe aquí tu código

t.left(90)
t.forward(100)


# ------------------------------------------
# Paso 4: Dibujar un cuadrado (sin bucle)
# ------------------------------------------
# Un cuadrado tiene:
# - 4 lados
# - 4 giros de 90 grados


# TODO:
# Completa los movimientos necesarios
# para dibujar un cuadrado de lado 100.
# Debes usar forward() y left() varias veces.
# La tortuga debe terminar donde empezó.

# Escribe aquí tu código
print("Dibujando un cuadrado sin bucle...")

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

# ------------------------------------------
# Paso 5: Dibujar un cuadrado usando un bucle
# ------------------------------------------
# Ahora haremos lo mismo pero usando menos código.


# TODO:
# Usa un bucle for que repita 4 veces:
#   - avanzar 100
#   - girar 90 grados

# for ...:
#     forward(...)
#     left(...)

print("Dibujando un cuadrado con bucle...")

for i in range(4):
    t.forward(100)
    t.left(90)

# ------------------------------------------
# Paso EXTRA (opcional)
# ------------------------------------------
# ¿Puedes dibujar un triángulo?
#
# Pista:
# - Un triángulo tiene 3 lados.
# - Un giro completo es 360 grados.
# - ¿Cuánto debe girar en cada esquina?

print("Dibujando un triangulo con bucle...")

for i in range(3):
    t.forward(100)
    t.left(120)
