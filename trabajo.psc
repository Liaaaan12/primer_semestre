Proceso metro

	Definir estudiantes, adulto, adul_M, usuarios, TipoUsuario, cant_usuarios, hora Como Entero;
//..................................................
	definir cont_estudiante, cont_adulto, cont_adul_M Como Entero;
	cont_estudiante = 0;
	cont_adulto = 0;
	cont_adul_M = 0;
	//hora
	hora<-azar(12);
//..................................................
	//valores normales
	Definir estu_nor,ad_nor,adMayor_nor Como Entero;
	estu_nor = 490;	
	ad_nor = 790;
	adMayor_nor = 390;
	
	//valores hora punta
	Definir estu_pun,ad_pun,adMayor_pun Como Entero;
	estu_pun = 590;	
	ad_pun = 890;
	adMayor_pun = 490;
//..................................................
	//total hora normal
	Definir total_estu,total_Adulto,total_General,total_AdMayor,total_Pagar Como Entero;
	//total hora punta
	Definir total_estu_pun,total_Adulto_pun,total_AdMayor_pun Como Entero;
	total_estu =0;
	total_estu_pun = 0;
	total_Adulto = 0;
	total_Adulto_pun = 0;
	total_AdMayor = 0;
	total_AdMayor_pun = 0;
	total_General = 0;
	total_Pagar = 0;
//..................................................
	Escribir "Hola!, bienvenido al metro milipilla";
	Escribir "actualmente son las: ", hora;
	Escribir "porfavor selecione la cantidad de personas";
	Leer Cant_usuarios;
//.................................................
	Escribir " ";
	Escribir "porfavor selecione el tipo de usuario";
	Escribir " ";
	Escribir "  Hora Normal";
	Escribir " [1] estudiante ";
	Escribir " [2] adulto ";
	Escribir " [3] adulto mayor ";
	Escribir " ";
	Escribir "  Hora Punta";
	Escribir " [4] estudiante ";
	Escribir " [5] adulto ";
	Escribir " [6] adulto mayor ";
	Escribir " ";
	leer usuarios;
//.................................................
	Escribir " ";
	si usuarios = usuarios Entonces
		
		si estu_nor = 1 Entonces
			Escribir "el tipo de entrada selecionado es: ", estu_nor;
			Escribir " ";
		
		FinSi
		
		escribir "el tipo de usuario selecionado es: ", usuarios;
		si ad_nor = 2 Entonces
			Escribir "el tipo de entrada selecionado es: ", ad_nor;
			Escribir " ";
			Escribir "el total a pagar es de: $790 pesos"; 
		FinSi
		
		escribir "el tipo de usuario selecionado es: ", usuarios;
		si adMayor_nor = 3 Entonces
			Escribir "el tipo de entrada selecionado es: ", adMayor_nor;
			Escribir " ";
			Escribir "el total a pagar es de: $390 pesos"; 
		FinSi
	FinSi
	//................................................
	Escribir " ";
	si usuarios = usuarios Entonces
		escribir "el tipo de usuario selecionado es: ", usuarios;
		si TipoEntrada = 4 Entonces
			Escribir "el tipo de entrada selecionado es: ", estu_pun;
			Escribir " ";
			Escribir "el total a pagar es de: $5.000 pesos"; 
		FinSi
		escribir "el tipo de usuario selecionado es: ", usuarios;
		si TipoEntrada = 5 Entonces
			Escribir "el tipo de entrada selecionado es: ", TipoEntrada;
			Escribir " ";
			Escribir "el total a pagar es de: $9.000 pesos"; 
		FinSi
		
	FinSi
	//.................................................
	
FinProceso
