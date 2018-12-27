from Cola import Cola
from Token import Token
from Tabla import Tabla
from FilaTabla import FilaTabla
from ALexico import ALexico
from ASintactico import ASintactico

class ASemantico:
	#Aunque inicialmente las tabalas se desarrollaban inicialmente en el analizador lexico, vamos a llevar todo el desarrollo de las tablas al analizador semantico por comodidad
	#Aqui debemos hacer comprobaciones como los tipos y las zonas en las que estamos
	#Zonas
	zona_funcion=False
	zona_switch=False
	zona_declaracion=False
	#Tipos (int,boolean, string, ok o error)
	id_tipo=""
	A_tipo=""
	B_tipo=""
	C_tipo=""
	E_tipo=""
	E1_tipo=""
	F_tipo=""
	H_tipo=""
	K_tipo=""
	L_tipo=""
	N_tipo=""
	P_tipo=""
	Q_tipo=""
	R_tipo=""
	R1_tipo=""
	S_tipo=""
	S1_tipo=""
	T_tipo=""
	U_tipo=""
	U1_tipo=""
	V_tipo=""
	V1_tipo=""
	X_tipo=""

	cola_tokens=Cola()#Cola de los tokens, vamos a coger la Cola de la que ha generado el Lexico
	cola_gram=Cola()#Cola de la situacion actual
	parse=[]#A eliminar, aqui no es necesario
	error=False
	terminales=["&=","(",")","+",",",":",";","<","=","bool","break","cadena","case","default","entero","function","id","if","int","print","prompt","return","string","switch","var","{","||","}"]
	fin=False
	desp=0
	desp_funcion=0
	desp_actual=0
	id_indice=""
	
	#Debido a la naturaleza de nuestra implementacion, vamos a volver a recorrer la tabla, pero esta vez vamos a fijarnos en los tipos y las zonas, de la misma forma que completaremos la tabla
	

	tabla_global=Tabla(None,"TABLA_GLOBAL")#Estado actual de la tabla global, ahora trabajaremos con ella
	tabla_funcion=None#Estado actual de la ultima tabla de funcion
	tabla_actual=None# #Puntero para saber sobre que tabla trabajamos
	#Para definir los tipos y manifestar errores en el semantico, vamos a definir una funcion especializada en ello, se anadira a la gramatica e iran definiendo las posibles situaciones

	def __init__(self,cola_tokens):
		self.cola_tokens=cola_tokens
		self.cola_tokens.encolar("$")
		self.cola_gram.encolar("P") #empezamos con la produccion
		self.tabla_actual=self.tabla_global#la primera tabla a la que apuntamos es la global

	def gestionSemantica(self, codigo_semantico):
		if(codigo_semantico=="SEM1"):#Entrada a declaracion de variable
			self.zona_switch=False
			self.zona_funcion=False
			self.zona_declaracion=True

		elif(codigo_semantico=="SEM2"):#Declaracion de variable
			self.id_tipo=self.T_tipo
			if (self.zona_declaracion==True):

				elemento=FilaTabla(self.id_indice.getExtra(),self.tabla_actual.getNombre())#Metemos el token en la tabla y comenzamos a meter datos
				if(self.tabla_actual.buscarEnTabla(elemento)==False):#No estaba ya declarado
					elemento.setTipo(self.id_tipo)
					elemento.setDesp(self.desp_actual)
					if(elemento.getTipo()=="int"):
						self.desp_actual=self.desp_actual+16

					elif(elemento.getTipo()=="bool"):
						self.desp_actual=self.desp_actual+2

					elif(elemento.getTipo()=="string"):
						self.desp_actual=self.desp_actual+200

					self.tabla_actual.insertarFila(elemento)
					self.id_indice.setExtra(self.tabla_actual.posicionEnTabla(elemento))	
					self.id_indice.escribirToken()#Ya podemos escribirlo
					self.tabla_actual.escrituraTabla(elemento)#escribimos en la tabla
				else:
					id_tipo="Error"
					print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : variable ya declarada"
					self.error=True

			else:
				id_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : declaracion en zona no permitida"
				self.error=True


		elif(codigo_semantico=="SEM3"):
			if(self.E_tipo=="bool"):
				B_tipo="ok"
			else:
				B_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : se esperaba una expresion booleana en la condicion del if"
				self.error=True

		elif(codigo_semantico=="SEM4"):
			self.zona_switch=True
			self.zona_funcion=False
			self.zona_declaracion=False

		elif(codigo_semantico=="SEM5"):
			if(self.E_tipo=="int"):
				self.B_tipo="ok"
			else:
				self.B_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : se esperaba una expresion entera en la expresion del switch"
				self.error=True

		elif(codigo_semantico=="SEM6"):
			self.B_tipo=self.S_tipo

		elif(codigo_semantico=="SEM7"):
			self.T_tipo="bool"

		elif(codigo_semantico=="SEM8"):
			self.T_tipo="int"

		elif(codigo_semantico=="SEM9"):
			self.T_tipo="string"

		elif(codigo_semantico=="SEM10"):
			elemento=FilaTabla(self.id_indice.getExtra(),self.tabla_actual.getNombre())
			if((self.tabla_actual.buscarEnTabla(elemento)==False) and (self.tabla_global.buscarEnTabla(elemento)==False)):#no estaba declarado
				elemento.setTipo("int")
				self.tabla_global.insertarFila(elemento)#insertamos en la tabla global
				self.id_tipo="int"#el tipo predeterminado, int
			elif(self.tabla_actual.buscarEnTabla(elemento)==True):#esta declarada en la tabla actual
				self.id_indice.setExtra(self.tabla_actual.posicionEnTabla(elemento))#ajustamos token
				self.id_indice.escribirToken()#escribimos token
				self.id_tipo=fila.getTipo()

		elif(codigo_semantico=="SEM11"):
			if(self.zona_funcion==False):
				self.S_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : no se puede usar return fuera de una funcion"
				self.error=True

			elif(self.X_tipo==self.H_tipo):
				self.S_tipo=self.X_tipo

			else:
				self.S_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : el return es de tipo distinto al definido para la funcion"
				self.error=True

		elif(codigo_semantico=="SEM12"):
			fila=self.tabla_actual.getFilaTabla(self.id_indice)
			self.id_tipo=fila.getTipo()
			if((self.id_tipo=="int") or (self.id_tipo=="string")):
				self.S_tipo="ok"
			else:
				self.S_tipo="error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : variable de tipo incorrecto dentro de un prompt"
				self.error=True

		elif(codigo_semantico=="SEM13"):
			if(self.zona_switch==True):
				self.S_tipo="ok"
			else:
				self.S_tipo="error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : break inesperado fuera de un switch"
				self.error=True

		elif(codigo_semantico=="SEM14"):
			if(self.E_tipo == self.id_tipo):
				self.S1_tipo="ok"
			else:
				self.S1_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : asignacion de tipos distintos"
				self.error=True
		elif(codigo_semantico=="SEM15"):
			if(self.E_tipo=="bool"):
				self.S1_tipo="ok"
			else:
				self.S1_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : los elementos de una asignacion logica deben ser de tipo logico"
				self.error=True

		elif(codigo_semantico=="SEM16"):
			self.X_tipo=self.E_tipo

		elif(codigo_semantico=="SEM17"):
			if (self.zona_switch==True):
				self.C_tipo="ok"
			else:
				self.C_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : case inesperado fuera de un switch"
				self.error=True

		elif(codigo_semantico=="SEM18"):
			if (self.zona_switch==True):
				self.C_tipo="ok"
			else:
				self.C_tipo="Error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : default inesperado fuera de un switch"
				self.error=True

		elif(codigo_semantico=="SEM19"):
			self.H_tipo=self.T_tipo

		elif(codigo_semantico=="SEM20"):
			self.V_tipo="int"

		elif(codigo_semantico=="SEM21"):
			self.V_tipo="string"

		elif(codigo_semantico=="SEM22"):#Creacion funcion
			self.zona_declaracion=True
			self.zona_switch=False
			self.zona_funcion=True

		elif(codigo_semantico=="SEM23"):#Creacion tabla funcion
			self.tabla_funcion=Tabla(self.tabla_global,"TABLA_FUNCION_"+self.id_indice.getExtra())#Creamos nueva tabla funcion
			#Preparamos el terreno para trabajar con ella, guardando el estado de la tabla global
			self.tabla_global=self.tabla_actual
			self.tabla_actual=self.tabla_funcion
			self.desp=self.desp_actual
			self.desp_funcion=0
			self.desp_actual=self.desp_funcion

		elif(codigo_semantico=="SEM24"): #fin de funcion
			zona_funcion=False
			#volvemos al estado de la tabla global
			self.tabla_actual=self.tabla_global
			self.desp_actual=self.desp

		elif(codigo_semantico=="SEM25"):
			self.E_tipo=self.R_tipo

		elif(codigo_semantico=="SEM26"):
			if(self.R_tipo=="bool" and self.E_tipo=="bool"):
				self.E1_tipo="ok"
			else:
				self.E1_tipo="error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : la operacion logica or requiere de booleanos"
				self.error=True

		elif(codigo_semantico=="SEM27"):
			self.R_tipo=self.U_tipo

		elif(codigo_semantico=="SEM28"):
			if(self.U_tipo=="int" and self.R_tipo=="int"):
				self.R1_tipo="ok"
			else:
				self.R1_tipo="error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : la operacion relacional menor que requiere de enteros"
				self.error=True

		elif(codigo_semantico=="SEM29"):
			self.U_tipo=self.V_tipo

		elif(codigo_semantico=="SEM30"):
			if(self.V_tipo=="int" and self.U_tipo=="int"):
				self.U1_tipo="ok"
			else:
				self.U1_tipo="error"
				print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : la operacion aritmetica suma requiere de enteros"
				self.error=True

		elif(codigo_semantico=="SEM31"):
			self.V_tipo=self.id_tipo

		elif(codigo_semantico=="SEM32"):
			self.V_tipo=self.E_tipo




	#La estructura de funcionamiento es similar al sintactico, solo que ahora tenemos que vigilar tanto estar en la zona correcta al declarar cosas como la correspondencia de tipos , a traves de SEM

	def recorrido(self):
		self.cola_gram.getElementos()
		self.cola_tokens.getElementos()


		#Lo primero es mirar con que elemento contamos en la cola de tokens y recorrer cada token
		#Debemos tomar los First y Follows como referenecias para saber como desplazarnos
		while (self.fin==False and self.error==False):
			print self.cola_gram.getElementos()
			print self.cola_tokens.getElementos()
			print self.cola_gram.mostrarUltimo()
			#print self.cola_tokens.mostrarPrimero().getId()
			#print self.cola_tokens.mostrarPrimero().getExtra()

			if(self.cola_tokens.estaVacia()):
				print "No hay nada que leer"
				self.error=True
			#Siguiendo la tabla, estudiamos que regla aplicamos para cada situacion
			elif(self.cola_gram.mostrarUltimo()=="A"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()

				if(self.cola_tokens.mostrarPrimero().getId()=="parentesis_cierre"):
					#lambda
					self.cola_gram.desencolarUltimo()
					self.parse.append("34")
				
				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra() in ["int" , "bool" , "string"]):

					#No hemos llegado al token, no desencolamos en la cadena
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("K")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("T")
					self.parse.append("33")
					#Insertamos los elementos al reves para respetar el formato de Cola creado para ALexico

				else:
					print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : se esperaba una definicion de tipo" 
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="B"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()

				if((self.cola_tokens.mostrarPrimero().getId()=="pal_res" and (self.cola_tokens.mostrarPrimero().getExtra() in ["break","print","prompt"])) or self.cola_tokens.mostrarPrimero().getId()=="identificador" ):
					#No hemos llegado al token, no desencolamos en la cadena
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM6")
					self.cola_gram.encolar("S")
					self.parse.append("7")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="if"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("S")
					self.cola_gram.encolar("SEM3")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("if")

					#Aqui si llegamos a if, asi que desencolamos tanto en la cadena como en el estado de la gramatica
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("5")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="switch"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("}")
					self.cola_gram.encolar("C")
					self.cola_gram.encolar("}")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("SEM5")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("SEM4")
					self.cola_gram.encolar("switch")
					#Hemos llegado a switch, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("6")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="var"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("SEM2")#Codigo semantico
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("T")
					self.cola_gram.encolar("SEM1")#Codigo semantico
					self.cola_gram.encolar("var")

					#Hemos llegado a var, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("4")
				else:
					print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : se esperaba una declaracion o sentencia"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="C"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()


				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="case"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("S")
					self.cola_gram.encolar(":")
					self.cola_gram.encolar("entero")
					self.cola_gram.encolar("SEM17")
					self.cola_gram.encolar("case")
					#Hemos llegado a case, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("21")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="default"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("S")
					self.cola_gram.encolar(":")
					self.cola_gram.encolar("SEM18")
					self.cola_gram.encolar("default")
					#Hemos llegado a default, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("22")

				elif(self.cola_tokens.mostrarPrimero().getId()=="llave_salida"):
					#lambda
					self.cola_gram.desencolarUltimo()
					self.parse.append("23")

				else:
					print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : sintaxis no permitida dentro de un switch"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="E"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()

				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_apertura","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("E1")
					self.cola_gram.encolar("SEM25")
					self.cola_gram.encolar("R")
					self.parse.append("37")
					#No hemos llegado al no terminal, no desencolamos
				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="E1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","Coma","PuntoYComa"]):
					#lambda
					self.cola_gram.desencolarUltimo()
					self.parse.append("39")

				elif(self.cola_tokens.mostrarPrimero().getId() == "op_logico"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("E1")
					self.cola_gram.encolar("SEM26")
					self.cola_gram.encolar("R")
					self.cola_gram.encolar("||")
					#Hemos llegado a default, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("38")

				else:
					print "Error en la linea " + str(self.cola_tokens.mostrarPrimero().getLinea()) + " : expresion incompleta"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="F"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="function"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM24")
					self.cola_gram.encolar("}")
					self.cola_gram.encolar("N")
					self.cola_gram.encolar("{")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("A")
					self.cola_gram.encolar("SEM23")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("H")
					self.cola_gram.encolar("SEM22")
					self.cola_gram.encolar("function")
					#Hemos llegado a function, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("28")

				else:
					print "Error"
			elif(self.cola_gram.mostrarUltimo()=="H"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["int","bool","string"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM19")
					self.cola_gram.encolar("T")
					self.parse.append("31")
					#no hemos llegado a un no terminal, no desencolamos

				elif(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("32")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="K"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="parentesis_cierre"):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("36")

				elif(self.cola_tokens.mostrarPrimero().getId()=="Coma"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("K")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("T")
					self.cola_gram.encolar(",")
					#Hemos llegado a coma, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("35")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="L"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_apertura","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("Q")
					self.cola_gram.encolar("E")
					self.parse.append("24")
					#No hemos llegado a un terminal, no desencolamos

				elif(self.cola_tokens.mostrarPrimero().getId()=="parentesis_cierre"):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("25")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="N"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("N")
					self.cola_gram.encolar("B")
					self.parse.append("29")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra() in ["break","if","print","prompt","return","switch","var"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("N")
					self.cola_gram.encolar("B")
					self.parse.append("29")

				elif(self.cola_tokens.mostrarPrimero().getId()=="llave_salida"):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("30")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="P"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()

				if(self.cola_tokens.mostrarPrimero()=="$"):
					print "Fin de cadena"
					self.parse.append("3")
					self.fin = True

				
				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra() in ["break","if","print","prompt","return","switch","var"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("P")
					self.cola_gram.encolar("B")
					self.parse.append("1") 

				elif(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("P")
					self.cola_gram.encolar("B")
					self.parse.append("1") 


				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="function"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("P")
					self.cola_gram.encolar("F")
					self.parse.append("2") 


				else:
					print "Error"
					self.error=True

			elif(self.cola_gram.mostrarUltimo()=="Q"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="Coma"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("Q")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar(",")
					#Hemos llegado a coma, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("26")

				elif(self.cola_tokens.mostrarPrimero().getId()=="parentesis_cierre"):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("27")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="R"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_apertura","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("R1")
					self.cola_gram.encolar("SEM27")
					self.cola_gram.encolar("U")
					self.parse.append("40")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="R1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="op_relacional"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("R1")
					self.cola_gram.encolar("SEM28")
					self.cola_gram.encolar("U")
					self.cola_gram.encolar("<")
					#Hemos llegado a <, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("41")

				elif(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","Coma","PuntoYComa","op_logico"]):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("42")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="S"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="break"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("SEM13")
					self.cola_gram.encolar("break")
					#Hemos llegado a ; , desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("15")

				elif(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("S1")
					self.cola_gram.encolar("SEM10")
					self.cola_gram.encolar("id")
					#Hemos llegado a id, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("11")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="print"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("print")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("13")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="prompt"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("SEM12")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("prompt")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("14")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="return"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM11")
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("X")
					self.cola_gram.encolar("return")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("12")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="S1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="op_asignacion" and self.cola_tokens.mostrarPrimero().getExtra()=="&="):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM15")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("&=")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("18")

				elif(self.cola_tokens.mostrarPrimero().getId()=="op_asignacion" and self.cola_tokens.mostrarPrimero().getExtra()=="="):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM14")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("=")
					#Hemos llegado a =, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("16")

				elif(self.cola_tokens.mostrarPrimero().getId()=="parentesis_apertura"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("L")
					self.cola_gram.encolar("(")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("17")

				else:
					self.error=True;
					print "Error"

			elif(self.cola_gram.mostrarUltimo()=="T"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="bool"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM7")
					self.cola_gram.encolar("bool")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("9")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="int"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM8")
					self.cola_gram.encolar("int")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("8")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="string"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM9")
					self.cola_gram.encolar("string")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("10")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="U"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_apertura","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("U1")
					self.cola_gram.encolar("SEM29")
					self.cola_gram.encolar("V")
					self.parse.append("43")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="U1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="op_aritmetico"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("U1")
					self.cola_gram.encolar("SEM30")
					self.cola_gram.encolar("V")
					self.cola_gram.encolar("+")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("44")

				elif(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","Coma","PuntoYComa","op_relacional","op_logico"] ):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("45")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="V"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="parentesis_apertura"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM32")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("(")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("47")

				elif(self.cola_tokens.mostrarPrimero().getId()=="cadena"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM21")
					self.cola_gram.encolar("cadena")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("49")

				elif(self.cola_tokens.mostrarPrimero().getId()=="entero"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM20")
					self.cola_gram.encolar("entero")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("48")

				elif(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM31")
					self.cola_gram.encolar("V1")
					self.cola_gram.encolar("identificador")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("46")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="V1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="parentesis_apertura"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("L")
					self.cola_gram.encolar("(")
					#Hemos llegado a print, desencolamos
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
					self.parse.append("50")

				elif(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","op_aritmetico","Coma","PuntoYComa","op_relacional","op_logico"]):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("51")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="X"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("SEM16")
					self.cola_gram.encolar("E")
					self.parse.append("19")

				elif(self.cola_tokens.mostrarPrimero().getId()=="PuntoYComa"):
					#lamda
					self.cola_gram.desencolarUltimo()
					self.parse.append("20")

				else:
					print "Error"
					self.error=True;
			elif(self.cola_gram.mostrarUltimo() in self.terminales):

				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_gram.mostrarUltimo()=="id"):
					self.id_indice=self.cola_tokens.mostrarPrimero()
					token=self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()
				else:
					token=self.cola_tokens.desencolarPrimero()
					token.escribirToken()
					self.cola_gram.desencolarUltimo()
			else:
				self.gestionSemantica(self.cola_gram.mostrarUltimo())#Si llegamos aqui, es un Sem. Veremos que hacer.
				self.cola_gram.desencolarUltimo()






