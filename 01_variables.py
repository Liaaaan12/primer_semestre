# Variables

my_string_variable = "My string variable"

print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas Funciones del sistema
print(len(my_string_variable))  # Lo que hace el 'len' es contar el total de los caracteres.  

#Variables en una sola linea . Cuidado con abusar de la sintaxis!
name, surname, alias, age = "Brais", " Moure", "MoureDev", 35
print("Me llamo", name, surname, ". Mi edad es: ", age, "Y mi alias es:", alias)

# Inputs (Pide los datos por teclado)
"""
name = input("Cual es tu nombre: ")
age = input('Cuantos annos tienes? ')
print(name)
print(age)
"""

#Cambiando su tipo

name = 35
age  = 'brais'

print(name)
print(age)

# Forzamos el tipo?
address: str ="Mi direccion"
address      = True
address      = 32
address      = 1.5
print (type(address))