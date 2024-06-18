Algoritmo sin_titulo
	Definir Nombre, Telefono Como Caracter;
	Definir aux, MenuMesas, PrecEst,PrecParcialEstandar Como Entero;
	
	aux = 1;
	PrecParcialEstandar = 0;
	PrecEst = 80000;
	ContEst = 0;
	PrecParcialAire = 0;
	PrecAire = 100000;
	ContAire = 0;
	PrecParcialVip = 0;
	PrecVip = 200000;
	ContVip = 0;
	
	
	Escribir "**********************************************************************";
	Escribir "bienvenido al sistema de reserva de mesas, ingrese los siguentes datos";
	Escribir "**********************************************************************";
	Escribir "Nombre";
	Leer Nombre;
	
	Mientras Longitud(Nombre) == 0 hacer 
		Escribir "porfavor escriba su Nombre: ";
		Leer Nombre;
	FinMientras
	
	Escribir "ingrese su numero de Telefono";
	Mientras Longitud(Telefono) == 0 hacer 
		Escribir "porfavor escriba su Telefono: ";
		Leer Telefono;
	FinMientras
	
	Escribir "El nombre ingresasdo es: " , Nombre;
	Escribir "El numero ingresado es: ", Telefono;
	
	Mientras aux == 1 Hacer
		Escribir "*******************************************";
		Escribir "escribir el tipo de mesa que desea reservar";
		Escribir "[1] Mesa normal";
		Escribir "[2] Mesa al aire libre";
		Escribir "[3] Mesa vip";
		Escribir "[4] Finalizar reserva";
		Escribir "*******************************************";
		leer MenuMesas;
	FinMientras
	
	Mientras (MenuMesas <> 1) y (MenuMesas <> 2) y (MenuMesas <> 3) y (MenuMesas <> 4) Hacer
		Escribir "Porfavor ingrese un numero del 1 y 4 de mesas, de acuerdo al menu";
		leer MenuMesas;
		
		si (MenuMesas == 1) Entonces
			PrecParcialEstandar = PrecParcialEstandar + PrecEst;  // acumulador
			ContEst = ContEst + 1;
			Escribir "Mesa Estandar Reservada";
		FinSi
		
		si (MenuMesas == 2) Entonces
			PrecParcialAire= PrecParcialAire + PrecAire;  // acumulador
			ContAire = ContAire + 1;
			Escribir "Mesa Aire Libre Reservada";
		FinSi
		
		si (MenuMesas == 3) Entonces
			PrecParcialVip = PrecParcialVip + PrecVip;  // acumulador
			ContVip = ContVip + 1;
			Escribir "Mesa Vip Reservada";
		FinSi
		
		si (MenuMesas == 4) Entonces
			aux =  1;
		FinSi
		
		si (ContEst = 0) y (ContAire = 0) Y (ContVip = 0) Entonces
			Escribir "No se ha reservado ninguna mesa, saliendo del progrma...";
		SiNo
			codVip = Aleatorio(100,200);
			codEst = Aleatorio(300,500);
			codAire = Aleatorio(600, 900);
			
			PrecioFinal = PrecParcialEstandar + PrecParcialAire + PrecParcialVip;
			
			Escribir " codigo vip", codVip;
			Escribir "Mesa Vip";
			Escribir "
			
		FinSi
		
	FinMientras
	
	
	
	
FinAlgoritmo
