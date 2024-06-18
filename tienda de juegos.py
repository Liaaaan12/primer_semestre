print("Hola bienvenido a GamerHause!")
print("Por favor ingresa tu nombre :)")

nombre = input()

juegos = {
    1: ("The Legend of Zelda: Breath of the Wild", 59990),
    2: ("Super Mario Odyssey", 49990),
    3: ("Mario Kart 8 Deluxe", 59990),
    4: ("Splatoon 2", 49990),
    5: ("ARMS", 39990),
    6: ("Xenoblade Chronicles 2", 59990),
    7: ("1-2-Switch", 49990),
    8: ("Kirby Star Allies", 59990),
    9: ("Bayonetta 2", 49990),
    10: ("Donkey Kong Country: Tropical Freeze", 59990),
    11: ("Hyrule Warriors: Definitive Edition", 49990),
    12: ("Captain Toad: Treasure Tracker", 39990),
    13: ("Pokkén Tournament DX", 59990),
    14: ("Mario Tennis Aces", 49990),
    15: ("Sushi Striker: The Way of Sushido", 39990),
    16: ("Octopath Traveler", 59990),
    17: ("Wolfenstein II: The New Colossus", 59990),
    18: ("Crash Bandicoot N. Sane Trilogy", 39990),
    19: ("Dark Souls: Remastered", 59990),
    20: ("Minecraft", 29990)
}

consolas = {
    1: ("Nintendo Switch", 299990),
    2: ("PlayStation 5", 499990),
    3: ("Xbox Series X", 499990),
    4: ("PC", 999990)
}

componentes = {
    1: ("Tarjeta de Gráficos", 399990),
    2: ("Procesador", 299990),
    3: ("RAM", 99990),
    4: ("Almacenamiento", 199990),
    5: ("Fuente de Poder", 149990)
}

accesorios = {
    1: ("Controlador", 59990),
    2: ("Audífonos", 79990),
    3: ("Cable de Carga", 19990),
    4: ("Mouse para Juegos", 49990),
    5: ("Teclado", 59990)
}

items_seleccionados = []

while True:
    print("\nHola "+ nombre + " ¿qué deseas comprar hoy?")
    print("1. Juegos")
    print("2. Consolas")
    print("3. Componentes")
    print("4. Accesorios")
    print("5. Nada")

    opcion = input()
    opcion = int(opcion)

    if opcion == 5:
        print("Gracias por tu compra")
        break

    if opcion == 1:
        print("Estos son los juegos que tenemos disponibles:")
        for key, value in juegos.items():
            print(f"{key}. {value[0]} - ${value[1]}")

        print("Ingresa el número del juego que deseas comprar:")
        juego = input()
        juego = int(juego)
        if juego >= 1 and juego <= 20:
            print("Ingresa la cantidad que deseas comprar:")
            cantidad = input()
            cantidad = int(cantidad)
            if cantidad > 0:
                items_seleccionados.append((juegos[juego][0], cantidad, juegos[juego][1]))
                print("Agregado al carrito:", cantidad, "x", juegos[juego][0])
            else:
                print("Cantidad inválida")
        else:
            print("Juego inválido")

    elif opcion == 2:
        print("Estas son las consolas que tenemos disponibles:")
        for key, value in consolas.items():
            print(f"{key}. {value[0]} - ${value[1]}")

        print("Ingresa el número de la consola que deseas comprar:")
        consola = input()
        consola = int(consola)
        if consola >= 1 and consola <= 4:
            print("Ingresa la cantidad que deseas comprar:")
            cantidad = input()
            cantidad = int(cantidad)
            if cantidad > 0:
                items_seleccionados.append((consolas[consola][0], cantidad, consolas[consola][1]))
                print("Agregado al carrito:", cantidad, "x", consolas[consola][0])
            else:
                print("Cantidad inválida")
        else:
            print("Consola inválida")

    elif opcion == 3:
        print("Estos son los componentes que tenemos disponibles:")
        for key, value in componentes.items():
            print(f"{key}. {value[0]} - ${value[1]}")

        print("Ingresa el número del componente que deseas comprar:")
        componente = input()
        componente = int(componente)
        if componente >= 1 and componente <= 5:
            print("Ingresa la cantidad que deseas comprar:")
            cantidad = input()
            cantidad = int(cantidad)
            if cantidad > 0:
                items_seleccionados.append((componentes[componente][0], cantidad, componentes[componente][1]))
                print("Agregado al carrito:", cantidad, "x", componentes[componente][0])
            else:
                print("Cantidad inválida")
        else:
            print("Componente inválido")

    elif opcion == 4:
        print("Estos son los accesorios que tenemos disponibles:")
        for key, value in accesorios.items():
            print(f"{key}. {value[0]} - ${value[1]}")

        print("Ingresa el número del accesorio que deseas comprar:")
        accesorio = input()
        accesorio = int(accesorio)
        if accesorio >= 1 and accesorio <= 5:
            print("Ingresa la cantidad que deseas comprar:")
            cantidad = input()
            cantidad = int(cantidad)
            if cantidad > 0:
                items_seleccionados.append((accesorios[accesorio][0], cantidad, accesorios[accesorio][1]))
                print("Agregado al carrito:", cantidad, "x", accesorios[accesorio][0])
            else:
                print("Cantidad inválida")
        else:
            print("Accesorio inválido")

    else:
        print("Opción inválida")

total = 0

print("\nBoleta de compra:")
for item, cantidad, precio in items_seleccionados:
    print(f"{item}: {cantidad} x ${precio}")
    total += cantidad * precio

print("Total a pagar:", total, "pesos chilenos")
