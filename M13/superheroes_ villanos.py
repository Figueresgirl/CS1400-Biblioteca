<<<<<<< HEAD
"""
Lógica del juego
Primero se crean dos jugadores, el héroe y el villano. Cada uno empieza con 100 puntos de vida y fuerza 0. Cuando el usuario presiona 'h', ambos jugadores generan una fuerza aleatoria entre 1 y 20. 
Luego se comparan las fuerzas. El que tenga la fuerza más baja pierde puntos de vida según la diferencia entre ambas fuerzas. Si ambos tienen la misma fuerza, nadie recibe daño. El juego termina cuando uno llega a 0 puntos de vida o cuando el usuario escribe 'q'. El programa usa programación orientada a objetos con una clase Player. Cada jugador tiene nombre, puntos de vida y fuerza. El método setStrength() genera una fuerza aleatoria y receiveDamage() resta puntos de vida.
 En cada ronda se comparan las fuerzas, y el jugador con menor fuerza recibe daño. El juego termina cuando uno se queda sin vida o el usuario sale.
"""
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.life_points = 100
        self.strength = 0

    def setStrength(self):
        self.strength = random.randint(1, 20)

    def receiveDamage(self, damage):
        self.life_points -= damage
        if self.life_points < 0:
            self.life_points = 0


def main():
    hero = Player("Spidey")
    villain = Player("Doc Oct")

    while hero.life_points > 0 and villain.life_points > 0:
        print("\nPuntos de vida de", hero.name + ":", hero.life_points)
        print("Puntos de vida de", villain.name + ":", villain.life_points)

        choice = input("\nPresiona 'h' para luchar o 'q' para salir: ")

        if choice == "q":
            print("\n¡Gracias por jugar!")
            break

        if choice == "h":
            hero.setStrength()
            villain.setStrength()

            print("\nFuerza de", hero.name + ":", hero.strength)
            print("Fuerza de", villain.name + ":", villain.strength)

            if hero.strength > villain.strength:
                damage = hero.strength - villain.strength
                villain.receiveDamage(damage)
                print(villain.name, "recibe", damage, "puntos de daño.")
            elif villain.strength > hero.strength:
                damage = villain.strength - hero.strength
                hero.receiveDamage(damage)
                print(hero.name, "recibe", damage, "puntos de daño.")
            else:
                print("Empate. Nadie recibe daño.")

    if hero.life_points == 0:
        print("\n¡" + villain.name + " gana la batalla!")
    elif villain.life_points == 0:
        print("\n¡" + hero.name + " gana la batalla!")


if __name__ == "__main__":
    main()

=======
"""
Lógica del juego
Primero se crean dos jugadores, el héroe y el villano. Cada uno empieza con 100 puntos de vida y fuerza 0. Cuando el usuario presiona 'h', ambos jugadores generan una fuerza aleatoria entre 1 y 20. 
Luego se comparan las fuerzas. El que tenga la fuerza más baja pierde puntos de vida según la diferencia entre ambas fuerzas. Si ambos tienen la misma fuerza, nadie recibe daño. El juego termina cuando uno llega a 0 puntos de vida o cuando el usuario escribe 'q'. El programa usa programación orientada a objetos con una clase Player. Cada jugador tiene nombre, puntos de vida y fuerza. El método setStrength() genera una fuerza aleatoria y receiveDamage() resta puntos de vida.
 En cada ronda se comparan las fuerzas, y el jugador con menor fuerza recibe daño. El juego termina cuando uno se queda sin vida o el usuario sale.
"""
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.life_points = 100
        self.strength = 0

    def setStrength(self):
        self.strength = random.randint(1, 20)

    def receiveDamage(self, damage):
        self.life_points -= damage
        if self.life_points < 0:
            self.life_points = 0


def main():
    hero = Player("Spidey")
    villain = Player("Doc Oct")

    while hero.life_points > 0 and villain.life_points > 0:
        print("\nPuntos de vida de", hero.name + ":", hero.life_points)
        print("Puntos de vida de", villain.name + ":", villain.life_points)

        choice = input("\nPresiona 'h' para luchar o 'q' para salir: ")

        if choice == "q":
            print("\n¡Gracias por jugar!")
            break

        if choice == "h":
            hero.setStrength()
            villain.setStrength()

            print("\nFuerza de", hero.name + ":", hero.strength)
            print("Fuerza de", villain.name + ":", villain.strength)

            if hero.strength > villain.strength:
                damage = hero.strength - villain.strength
                villain.receiveDamage(damage)
                print(villain.name, "recibe", damage, "puntos de daño.")
            elif villain.strength > hero.strength:
                damage = villain.strength - hero.strength
                hero.receiveDamage(damage)
                print(hero.name, "recibe", damage, "puntos de daño.")
            else:
                print("Empate. Nadie recibe daño.")

    if hero.life_points == 0:
        print("\n¡" + villain.name + " gana la batalla!")
    elif villain.life_points == 0:
        print("\n¡" + hero.name + " gana la batalla!")


if __name__ == "__main__":
    main()

>>>>>>> 14b53114c557d2ca8e70cec2befd625274d6a4e5
