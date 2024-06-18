def calcular_total(sandwiches):
    precios = {
        "Churrasco": 1500,
        "Completo": 1000,
        "Vegetariano": 2000,
        "Barros Luco": 3000
    }
    total = sum(precios[sandwich] * cantidad for sandwich, cantidad in sandwiches.items())
    return total

def aplicar_descuento(total, codigo_descuento):
    if codigo_descuento == "Descuento10":
        total_descuento = total * 0.1
        total -= total_descuento
    return total

def main():
    sandwiches = {
        "Churrasco": int(input("Cantidad de sándwiches Churrasco: ")),
        "Completo": int(input("Cantidad de sándwiches Completo: ")),
        "Vegetariano": int(input("Cantidad de sándwiches Vegetariano: ")),
        "Barros Luco": int(input("Cantidad de sándwiches Barros Luco: "))
    }

    total = calcular_total(sandwiches)

    codigo_descuento = input("Ingrese su código de descuento (si no tiene, presione Enter): ").strip().upper()

    total_con_descuento = aplicar_descuento(total, codigo_descuento)

    print(f"Total a pagar: ${total_con_descuento}")

if __name__ == "__main__":
    main()

