#Listas

lista= [1, 2, 4, 5]

#La funcion de agregar, nos inserta el dato al final de la lista
lista.append(6)
lista.append("Alenjandro")
print(lista)

#-----------------------------------------------
#Si queremos agregar en una posicion especifica UN SOLO DATO

lista.insert(2, 3)
#Primero se le pasa el indice(Posicion en la lista) y luego el valor que queremos agregar


#-----------------------------------------------

#Si queremos agregar varios elementos al final de la lista

lista.extend([6, 7, 8])
print(lista)

#----------------------------------------------
#Para concatenar listas, simplemente las sumamos

lista1= [1, 2, 3, 4, 5]
lista2= [6, 7 , 8]
lista3= lista1 + lista2
print(lista3)
print(lista3)

#-----------------------------------------------
#Si queremos buscar determinados elementos en la lista

lista9= [1, 2, 3, 4, 5, "Alejandro", 1, 2, 3, 1, "Alejandro", 1]

print(10 in lista9) #Ocupamos esta forma


#-----------------------------------------------
#Si queremos saber exactamente en que indice se ubica dicho elemento

print(lista9.index(5)) #Ocupamos esta forma


#-----------------------------------------------
#Para determinar cuantos valores existen en la lista de determinado elemento, ya sea que este repetido o solo este uno solo

print(lista9.count(1))
#Entonces esto nos va a indicar cuantos valores 1 hay en la lista 

#------------------------------------------------
#Ahora se vera como eliminar un dato en una lista

lista9.pop()
#Si no le colocamos el indice especifico que queremos borrar, al ejecutarlo vacio, este solo va eliminar el ultimo elementop en la lista
lista9.pop(2)
#Aqui eliminaria el indice dos, que equivale al numero 3 de la lista original


#Otro metodo que permite eliminar sin que nosotros sepamos el indice o en que lugar esta ubicado
lista.remove(5)
#Solo le pasamos el dato que queremos eliminar y lo eliminara de la lista, o simplemente si lo dejamos vacio, este eliminara el ultimo elemento en la lista.


#Si queremos eliminar toda la lista, para que esta quede vacia usamos
lista9.clear()

#---------------------------------------------------

#Si queremos que la lista se de vuelta, usamos

lista9.reverse()

#---------------------------------------------------

#Si queremos que los elementos se copien dos veces en el mismo orden, multimplicamos con el numero de veces que queramos
lista6=[1, 2, 3, 4, 5, "Alejandro"] *2

#---------------------------------------------------

#Para ordenar una lista de enteros

lista7= [5, 4, -7, 9, 0, 1, 3]
#Aqui se ordenan de menor a mayor
lista7.sort()

#Aqui se ordenan de mayor a menor
lista7.sort(reverse=True)




