### Operadores Arritmeticos ###

print(3 + 4)     # Suma.
print(3 - 4)     # Resta.
print(3 * 4)     # Multiplicacion.
print(3 / 4)     # Divicion.
print(10 % 3)    # El modulo es el resto al final de la divicion.
print(10 // 3)   # For divicion, Lo que hace es que en ves de aproximar el resultado de la divicion a un dicimal, lo que hace es aproximarla a un numero entero siempre.
print(2 ** 3)    # Calcular un exponente, O calcula el elevado.

print("Hola "  +  "Python " + "Que tal?")
print("Hola "  + str(5))
print("Hola " * 5)
print("Hola " *(2 **3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)    # Mayor que
print(3 < 4)    # Menor que  
print(3 >= 4)   # Mayor o igual que
print(4 <= 4)   # Menor o igual
print(3 == 4)   # Igual
print(3 != 4)   # Distinto 

print("Hola" > "Python")    
print("Hola" < "Python")    
print("aaaa" >= "abaa")  # Ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa"))   # Cuenta caracteres
print("Hola" <= "Python")  
print("Hola" == "Python")   
print("Hola" != "Python")

### Operadores Logicos ###

print(3 > 4 and "Hola" > "Python") 
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or ("Hola" < "Python" and 4 == 4))  
print(not (3 > 4)) # Este not es para negar toda la condicion

print("Hola")
