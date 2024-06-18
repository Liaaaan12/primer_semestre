import random

class RuletaPoker:
    def __init__(self, jugador, dinero):
        self.jugador = jugador
        self.dinero = dinero
        self.resultado = None

    def girar_ruleta(self):
        self.resultado = random.randint(1, 36)

    def apostar(self, numero_apostado, cantidad_apostada):
        if cantidad_apostada > self.dinero:
            print("No tienes suficiente dinero para esta apuesta.")
            return
        self.dinero -= cantidad_apostada
        self.girar_ruleta()
        if self.resultado == numero_apostado:
            self.dinero += cantidad_apostada * 36
            return cantidad_apostada * 36
        else:
            return 0

def main():
    print("Bienvenido a la Ruleta de Poker")
    jugador = input("Por favor, ingresa tu nombre: ")
    dinero = int(input("Ingresa la cantidad de dinero que quieres jugar: "))
    ruleta = RuletaPoker(jugador, dinero)

    while ruleta.dinero > 0:
        print("\n--- Nuevo juego ---")
        print(f"Dinero disponible: ${ruleta.dinero}")
        numero_apostado = int(input("Elige un número para apostar (1-36): "))
        cantidad_apostada = int(input("Ingresa la cantidad que deseas apostar: "))

        if numero_apostado < 1 or numero_apostado > 36:
            print("Número inválido. Debes apostar a un número entre 0 y 36.")
            continue

        if cantidad_apostada > ruleta.dinero:
            print("No tienes suficiente dinero para esta apuesta.")
            continue

        premio = ruleta.apostar(numero_apostado, cantidad_apostada)

        if premio > 1:
            print(f"Felicidades {jugador}, has ganado ${premio}!")
        else:
            print("Lo siento, no has ganado esta vez.")

    print("\n--- Juego terminado ---")
    print(f"Resumen final para {jugador}:")
    print(f"Dinero inicial: ${dinero}")
    print(f"Dinero final: ${ruleta.dinero}")
    print(f"Has {'ganado' if ruleta.dinero > dinero else 'perdido'} ${abs(dinero - ruleta.dinero)}")

if __name__ == "__main__":
    main()






