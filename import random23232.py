import random

class Casino:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.saldo = 0
        self.resultado_juegos = []

    def ingresar_saldo(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se han agregado {monto} fichas a tu cuenta. Saldo actual: {self.saldo} fichas.")
        else:
            print("El monto ingresado no es válido.")

    def jugar_ruleta(self, apuesta):
        if self.saldo >= apuesta:
            numero_ganador = random.randint(0, 36)
            if apuesta.isdigit() and 0 <= int(apuesta) <= self.saldo:
                apuesta = int(apuesta)
                if apuesta <= self.saldo:
                    if apuesta == numero_ganador:
                        self.saldo += 36 * apuesta
                        self.resultado_juegos.append(f"Ruleta: Acertaste! Ganaste {36 * apuesta} fichas.")
                    else:
                        self.saldo -= apuesta
                        self.resultado_juegos.append(f"Ruleta: No acertaste. Perdiste {apuesta} fichas.")
            else:
                self.resultado_juegos.append("Ruleta: Apuesta no válida o saldo insuficiente.")
        else:
            print("No tienes saldo suficiente para realizar esa apuesta.")

    def jugar_tragamonedas(self, apuesta):
        if self.saldo >= apuesta:
            combinaciones = ["🍒🍒🍒", "🍋🍋🍋", "🔔🔔🔔", "💎💎💎", "7️⃣7️⃣7️⃣"]
            resultado = random.choice(combinaciones)
            if resultado == "🍒🍒🍒":
                self.saldo += 10 * apuesta
                self.resultado_juegos.append(f"Tragamonedas: ¡Ganaste! 10 veces tu apuesta: {10 * apuesta} fichas.")
            elif resultado == "🍋🍋🍋":
                self.saldo += 5 * apuesta
                self.resultado_juegos.append(f"Tragamonedas: ¡Ganaste! 5 veces tu apuesta: {5 * apuesta} fichas.")
            elif resultado == "🔔🔔🔔":
                self.saldo += 20 * apuesta
                self.resultado_juegos.append(f"Tragamonedas: ¡Ganaste! 20 veces tu apuesta: {20 * apuesta} fichas.")
            elif resultado == "💎💎💎":
                self.saldo += 50 * apuesta
                self.resultado_juegos.append(f"Tragamonedas: ¡Ganaste! 50 veces tu apuesta: {50 * apuesta} fichas.")
            elif resultado == "7️⃣7️⃣7️⃣":
                self.saldo += 100 * apuesta
                self.resultado_juegos.append(f"Tragamonedas: ¡Jackpot! Ganaste 100 veces tu apuesta: {100 * apuesta} fichas.")
        else:
            print("No tienes saldo suficiente para realizar esa apuesta.")

    def retirar_dinero(self):
        print(f"Saldo actual: {self.saldo} fichas")
        if self.saldo > 0:
            print("¿Cómo te gustaría retirar tu dinero?")
            print("1. Efectivo")
            print("2. Transferencia Bancaria")
            print("3. Tarjeta de Crédito")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                metodo_pago = "Efectivo"
            elif opcion == "2":
                metodo_pago = "Transferencia Bancaria"
            elif opcion == "3":
                metodo_pago = "Tarjeta de Crédito"
            else:
                print("Opción no válida.")
                return

            print(f"Retirando {self.saldo} fichas usando {metodo_pago}")

            boleta = f"Nombre: {self.nombre}\nRUT: {self.rut}\n"
            boleta += "Detalles de la transacción:\n"
            for resultado in self.resultado_juegos:
                boleta += resultado + "\n"
            boleta += f"Total retirado: {self.saldo} fichas\nMétodo de pago: {metodo_pago}"
            print(boleta)

            self.saldo = 0
        else:
            print("No tienes saldo para retirar.")

def inicio_sesion():
    print("¡Bienvenido al Casino!")
    nombre = input("Por favor, ingresa tu nombre: ")
    rut = input("Por favor, ingresa tu RUT: ")
    saldo = int(input("Por favor, ingresa el saldo con el que deseas jugar: "))

    jugador = Casino(nombre, rut)
    jugador.ingresar_saldo(saldo)

    menu_principal(jugador)

def menu_principal(jugador):
    while True:
        print("\nMenú Principal:")
        print("1. Jugar a la Ruleta")
        print("2. Jugar a las Tragamonedas")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            apuesta = input(f"Saldo actual: {jugador.saldo} fichas\nIngresa tu apuesta (entre 0 y {jugador.saldo}): ")
            jugador.jugar_ruleta(apuesta)
        elif opcion == "2":
            apuesta = int(input(f"Saldo actual: {jugador.saldo} fichas\nIngresa tu apuesta: "))
            jugador.jugar_tragamonedas(apuesta)
        elif opcion == "3":
            jugador.retirar_dinero()
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

inicio_sesion()
