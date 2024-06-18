Proceso Parque_Diversiones
	Definir Edadmenor, Edadadulto, Edad_adulto_mayor, edad, menor, adulto, adultoMayor Como Entero;
	Definir cantidad, usuarios Como Entero;
	Definir descuento, totalgeneral, totalmenor, totaladulto, totaladultoM Como real;
	
//................................................
    Escribir "Hola! bienvenido!"; 
	escribir "porfavor escriba la cantidad de su grupo";
	leer cantidad;
	
	cantidad = 0;
	descuento = 0;
	Edadadulto = 0;
	Edadmenor = 0;
	Edad_adulto_mayor = 0;
	
//................................................
	
	Escribir "  ";
	Escribir "cuantos menores son?";
	leer cantidad;
	Escribir "cuantos adultos son?";
	leer cantidad;
	Escribir "cuantos adultos mayores son?";
	leer cantidad;
	
//................................................
	
	mientras contador < usuarios hacer;
		escribir "ingrese la edad: ";
		leer edad;
		
		si edad <= 13 Entonces
			Edadmenor = Edadmenor + 1;
			totalmenor = Edadmenor * menor;
		FinSi
		
		si edad >= 14 y <= 64 Entonces
			Edadmenor = Edadmenor + 1;
			totalmenor = Edadmenor * menor;
		FinSi
		
		
	FinMientras
	
	
	
FinProceso
