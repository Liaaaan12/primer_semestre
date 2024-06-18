### Strings ###

my_string = "Mi String"
my_other_string  = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " +my_other_string)

my_new_line_string = "Este es un String \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapando"
print(my_scape_string)

# Formateo 

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Dos formas de hacerlo XD
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " " + "y mi edad es " + str(age)) # No recomendado (ineficiente)
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Esta es la mas recomendada

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e,f = "Python" 
print(a)
print(e)

# Division

language_slice = language[1:3] # La primera letra cuenta como 0 a la hora de contar.
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2] # Rebuscado XD
print(language_slice)

# Reversed

reversed_language = language[::-1]
print(reversed_language)


