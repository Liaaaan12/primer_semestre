class Persona:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

class AlmacenamientoDatos:
    def __init__(self):
        self.datos = []

    def agregar_persona(self, persona):
        self.datos.append(persona)

    def mostrar_datos(self):
        if len(self.datos) == 0:
            print("No hay datos ingresados.")
        else:
            for persona in self.datos:
                print(f"Nombre: {persona.nombre}")
                print(f"Apellido: {persona.apellido}")
                print(f"Edad: {persona.edad}")
                print(f"Ciudad: {persona.ciudad}")
                print("--------------------")

almacenamiento = AlmacenamientoDatos()

while True:
    print("1. Agregar persona")
    print("2. Mostrar datos")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = input("Ingrese la edad: ")
        ciudad = input("Ingrese la ciudad: ")

        persona = Persona(nombre, apellido, edad, ciudad)
        almacenamiento.agregar_persona(persona)
        print("Persona agregada exitosamente.")
    elif opcion == "2":
        almacenamiento.mostrar_datos()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
