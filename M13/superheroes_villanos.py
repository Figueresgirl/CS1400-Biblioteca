
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
    hero = Player("Taisa")
    villain = Player("Doc April")

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

    # Resultado final
    if hero.life_points == 0:
        print("\n¡" + villain.name + " gana la batalla!")
    elif villain.life_points == 0:
        print("\n¡" + hero.name + " gana la batalla!")
    else:
        print("\nJuego terminado por el usuario.")


if __name__ == "__main__":
    main()
