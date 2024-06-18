from fileinput import lineno
import random

class Casino:
    def __init__(self, jugador, dinero):
        self.jugador = jugador
        self.dinero = dinero
        self.resultado = None

    def girar_ruleta(self):
        """ Simula el giro de la ruleta y genera un número aleatorio entre 0 y 36. """
        self.resultado = random.randint(0, 36)

    def jugar_ruleta(self):
        """ Permite al jugador jugar a la ruleta de poker. """
        print("\n--- Ruleta de Poker ---")
        numero_apostado = self.obtener_numero("Elige un número para apostar (0-36): ", 0, 36)
        cantidad_apostada = self.obtener_cantidad("Ingresa la cantidad que deseas apostar: ")

        if cantidad_apostada > self.dinero:
            print("No tienes suficiente dinero para esta apuesta.")
            return

        self.dinero -= cantidad_apostada
        self.girar_ruleta()
        if self.resultado == numero_apostado:
            premio = cantidad_apostada * 36
            self.dinero += premio
            print(f"Felicidades {self.jugador}, has ganado ${premio}!")
        else:
            print("Lo siento, no has ganado esta vez.")

    def jugar_blackjack(self):
        """ Permite al jugador jugar al Blackjack. """
        print("\n--- Blackjack ---")
        print("El objetivo del Blackjack es sumar 21 o acercarse lo más posible sin pasarse.\n\
Si la suma de tus cartas supera 21, pierdes.\n\
Si la suma de tus cartas es igual a 21, ganas automáticamente.\n\
Si la suma de tus cartas es menor que 21, puedes 'plantarte' o 'pedir' otra carta.")
        
        def valor_carta(carta):
            if carta in ('J', 'Q', 'K'):
                return 10
            elif carta == 'A':
                return 11
            else:
                return int(carta)

        def valor_mano(mano):
            valor = sum(valor_carta(carta[0]) for carta in mano)
            # Si la mano contiene un As y supera 21, convierte el As a valor 1
            for carta in mano:
                if carta[0] == 'A' and valor > 21:
                    valor -= 10
            return valor

        def mostrar_mano(mano):
            print("Cartas en tu mano:")
            for carta in mano:
                print(f"   {carta}")

        def blackjack():
            return len(jugador) == 2 and valor_mano(jugador) == 21

        def resultado(jugador, crupier):
            if valor_mano(jugador) > 21:
                return 'pierdes'
            elif valor_mano(crupier) > 21 or valor_mano(jugador) > valor_mano(crupier):
                return 'ganaste'
            elif valor_mano(jugador) == valor_mano(crupier):
                return 'empate'
            else:
                return 'pierdes'

        while True:
            jugador = [random.choice('23456789JQKA') for _ in range(2)]
            crupier = [random.choice('23456789JQKA') for _ in range(2)]
            print("\nCartas del crupier:")
            print(f"   {crupier[0]}")
            print("Cartas en tu mano:")
            print(f"   {jugador[0]}")
            print(f"   {jugador[1]}")

            if blackjack():
                print("¡Blackjack! ¡Ganas automáticamente!")
                self.dinero += 1.5 * cantidad_apostada # type: ignore
            else:
                while valor_mano(jugador) < 21:
                    opcion = input("¿Quieres plantarte (p) o pedir otra carta (c)? ").lower()
                    if opcion == 'c':
                        carta = random.choice('23456789JQKA')
                        jugador.append(carta)
                        print(f"Has recibido: {carta}")
                        mostrar_mano(jugador)
                        if blackjack():
                            print("¡Blackjack! ¡Ganas automáticamente!")
                            self.dinero += 1.5 * cantidad_apostada # type: ignore
                            break
                    else:
                        break

                mostrar_mano(crupier)
                while valor_mano(crupier) < 17:
                    carta = random.choice('23456789JQKA')
                    crupier.append(carta)
                    print(f"El crupier ha recibido: {carta}")
                    mostrar_mano(crupier)

                print(f"\nTus cartas suman: {valor_mano(jugador)}")
                print(f"Las cartas del crupier suman: {valor_mano(crupier)}")
                print(f"Resultado: {resultado(jugador, crupier)}")
                if resultado(jugador, crupier) == 'ganaste':
                    self.dinero += cantidad_apostada # type: ignore
                elif resultado(jugador, crupier) == 'pierdes':
                    self.dinero -= cantidad_apostada # type: ignore
            break

    def jugar_tragamonedas(self):
        """ Permite al jugador jugar a las tragamonedas. """
        print("\n--- Tragamonedas ---")
        print("Elige 3 números entre 0 y 9.")
        numero_apostado_1 = self.obtener_numero("Primer número: ", 0, 9)
        numero_apostado_2 = self.obtener_numero("Segundo número: ", 0, 9)
        numero_apostado_3 = self.obtener_numero("Tercer número: ", 0, 9)
        cantidad_apostada = self.obtener_cantidad("Ingresa la cantidad que deseas apostar: ")

        if cantidad_apostada > self.dinero:
            print("No tienes suficiente dinero para esta apuesta.")
            return

        self.dinero -= cantidad_apostada

        numeros_generados = [random.randint(0, 9) for _ in range(3)]
        print(f"\nLos números generados son: {numeros_generados[0]} {numeros_generados[1]} {numeros_generados[2]}")

        aciertos = 0
        if numero_apostado_1 in numeros_generados:
            aciertos += 1
        if numero_apostado_2 in numeros_generados:
            aciertos += 1
        if numero_apostado_3 in numeros_generados:
            aciertos += 1

        if aciertos == 3:
            premio = cantidad_apostada * 5
            self.dinero += premio
            print(f"Felicidades {self.jugador}, has ganado ${premio}!")
        elif aciertos == 2:
            premio = cantidad_apostada * 2
            self.dinero += premio
            print(f"¡Has acertado 2 números! Has ganado ${premio}!")
        elif aciertos == 1:
            premio = cantidad_apostada * 1
            self.dinero += premio
            print(f"¡Has acertado 1 número! Has ganado ${premio}!")
        else:
            print("Lo siento, no has ganado esta vez.")

    def vida_o_muerte(self):
        """ Ofrece al jugador la opción de continuar jugando o salir del juego. """
        print("\n--- Vida o Muerte ---")
        decision = input("Tu saldo es negativo. ¿Deseas seguir jugando? (s/n): ")
        if decision.lower() == 's':
            self.dinero = 1000
            print("Te han dado una segunda oportunidad. Tu saldo ha sido restablecido a $1000.")
        else:
            print("Lo siento, has elegido salir del juego.")
            exit()

    def jugar(self):
        """ Inicia el casino y permite al jugador elegir un juego para jugar. """
        while self.dinero > 0:
            print(f"\n--- Bienvenido al Casino ---\nJugador: {self.jugador}\nDinero disponible: ${self.dinero}")
            print("\n1. Ruleta de Poker\n2. Blackjack\n3. Tragamonedas\n4. Salir")
            opcion = input("Elige el número del juego que quieres jugar (1-4): ")

            if opcion == '1':
                self.jugar_ruleta()
            elif opcion == '2':
                self.jugar_blackjack()
            elif opcion == '3':
                self.jugar_tragamonedas()
            elif opcion == '4':
                print("\nGracias por jugar. ¡Hasta luego!")
                exit()
            else:
                print("\nOpción no válida. Por favor, elige un número del 1 al 4.")

            if self.dinero < 0:
                self.vida_o_muerte()

        print("\n--- Juego terminado ---")
        print(f"Resumen final para {self.jugador}:")
        print(f"Dinero inicial: ${lineno}")
        print(f"Dinero final: ${self.dinero}")
        print(f"Has {'ganado' if self.dinero > dinero else 'perdido'} ${abs(dinero - self.dinero)}") # type: ignore

    def obtener_numero(self, mensaje, minimo, maximo):
        """Valida y devuelve un número entero dentro del rango especificado."""
        while True:
            try:
                numero = int(input(mensaje))
                if minimo <= numero <= maximo:
                    return numero
                else:
                    print(f"Por favor, ingresa un número entre {minimo} y {maximo}.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def obtener_cantidad(self, mensaje):
        """Valida y devuelve una cantidad de dinero como número entero."""
        while True:
            try:
                cantidad = int(input(mensaje))
                if cantidad > 0:
                    return cantidad
                else:
                    print("Por favor, ingresa una cantidad válida mayor que 0.")
            except ValueError:
                print("Por favor, ingresa una cantidad válida.")

def main():
    print("Bienvenido al Casino")
    jugador = input("Por favor, ingresa tu nombre: ")
    dinero = Casino().obtener_cantidad("Ingresa la cantidad de dinero que quieres jugar: ") # type: ignore
    casino = Casino(jugador, dinero)
    casino.jugar()

if __name__ == "__main__":
    main()
