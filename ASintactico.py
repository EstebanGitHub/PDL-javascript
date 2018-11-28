from Cola import Cola
from Token import Token
from Tabla import Tabla
from FilaTabla import FilaTabla
from ALexico import ALexico

class ASintactico:
	#Nuestro analizador es descendiente por tablas
	cola_tokens=Cola()#Cola de los tokens, vamos a coger la Cola de la que ha generado el Lexico
	cola_gram=Cola()#Cola de la situacion actual
	tabla_global=Tabla(None,"TABLA_BASE")#Estado actual de la tabla global, ahora trabajaremos con ella
	tablas_funciones=[]
	parse=[]
	error=False
	terminales=["&=","(",")","+",",",":",";","<","=","bool","break","cadena","case","default","entero","function","id","if","int","print","prompt","return","string","switch","var","{","||","}"]

	


	def __init__(self,cola_tokens, tabla_global, tablas_funciones):
		self.cola_tokens=cola_tokens
		self.cola_tokens.encolar("$")
		self.cola_gram.encolar("P") #empezamos con la produccion
		self.tabla_global=tabla_global
		self.lista_tablas_funciones=tablas_funciones

	#Tenemos que construir una nueva gramatica que realice el comportamiento de un analizador sintactico, debido a que su gramatica es de tipo 2, tenemos que controlar en todo momento en que situacion estamos
	#Aqui ya tenemos la cola por defecto y ya no tenemos que leer nada
	def recorrido(self):
		self.cola_gram.getElementos()
		self.cola_gram.getElementos()
		self.cola_tokens.getElementos()


		#Lo primero es mirar con que elemento contamos en la cola de tokensy recorrer cada token
		#Debemos tomar los First y Follows como referenecias para saber como desplazarnos
		while (self.cola_tokens.mostrarPrimero()!="$" and self.error==False):
			print self.cola_gram.getElementos()
			print self.cola_tokens.getElementos()
			print self.cola_gram.mostrarUltimo()
			print self.cola_tokens.mostrarPrimero().getId()
			print self.cola_tokens.mostrarPrimero().getExtra()

			if(self.cola_tokens.estaVacia()):
				print "No hay nada que leer"
				self.error=True
			#Siguiendo la tabla, estudiamos que regla aplicamos para cada situacion
			elif(self.cola_gram.mostrarUltimo()=="A"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()

				if(self.cola_tokens.mostrarPrimero().getId()=="parentesis_apertura"):
					#lambda
					self.cola_gram.desencolarUltimo()
				
				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra() in ["int" , "bool" , "string"]):

					#No hemos llegado al token, no desencolamos en la cadena
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("K")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("T")
					#Insertamos los elementos al reves para respetar el formato de Cola creado para ALexico

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="B"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()

				if((self.cola_tokens.mostrarPrimero().getId()=="pal_res" and (self.cola_tokens.mostrarPrimero().getExtra() in ["break","print","prompt"])) or self.cola_tokens.mostrarPrimero().getId()=="identificador" ):
					#No hemos llegado al token, no desencolamos en la cadena
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("S")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="if"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("S")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("if")
					#Aqui si llegamos a if, asi que desencolamos tanto en la cadena como en el estado de la gramatica
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="switch"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("}")
					self.cola_gram.encolar("C")
					self.cola_gram.encolar("}")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("switch")
					#Hemos llegado a switch, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="var"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("T")
					self.cola_gram.encolar("var")
					#Hemos llegado a var, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()
				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="C"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()


				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="case"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("S")
					self.cola_gram.encolar(":")
					self.cola_gram.encolar("entero")
					self.cola_gram.encolar("case")
					#Hemos llegado a case, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="default"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("S")
					self.cola_gram.encolar(":")
					self.cola_gram.encolar("default")
					#Hemos llegado a default, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="llave_cierre"):
					#lambda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="E"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()

				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_apertura","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("E1")
					self.cola_gram.encolar("R")
					#No hemos llegado al no terminal, no desencolamos
				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="E1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","Coma","PuntoYComa"]):
					#lambda
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId() == "op_logico"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("E1")
					self.cola_gram.encolar("R")
					self.cola_gram.encolar("||")
					#Hemos llegado a default, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="F"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="function"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("}")
					self.cola_gram.encolar("N")
					self.cola_gram.encolar("{")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("A")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("H")
					self.cola_gram.encolar("function")
					#Hemos llegado a function, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
			elif(self.cola_gram.mostrarUltimo()=="H"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["int","bool","string"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("T")
					#no hemos llegado a un no terminal, no desencolamos

				elif(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					#lamda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="K"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="parentesis_cierre"):
					#lamda
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="Coma"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("K")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("T")
					self.cola_gram.encolar(",")
					#Hemos llegado a coma, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="L"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_apertura","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("Q")
					self.cola_gram.encolar("E")
					#No hemos llegado a un terminal, no desencolamos

				elif(self.cola_tokens.mostrarPrimero().getId()=="parentesis_cierre"):
					#lamda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="N"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("N")
					self.cola_gram.encolar("B")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra() in ["break","if","print","prompt","return","switch","var"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("N")
					self.cola_gram.encolar("B")

				elif(self.cola_tokens.mostrarPrimero().getId()=="llave_cierre"):
					#lamda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="P"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				
				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra() in ["break","if","print","prompt","return","switch","var"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("P")
					self.cola_gram.encolar("B")

				elif(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("P")
					self.cola_gram.encolar("B")


				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="function"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("P")
					self.cola_gram.encolar("F")

				elif(self.cola_tokens.mostrarPrimero().getId()=="$"):
					print "Fin de cadena"

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="Q"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="Coma"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("Q")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar(",")
					#Hemos llegado a coma, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="parentesis_cierre"):
					#lamda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="R"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_apertura","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("R1")
					self.cola_gram.encolar("U")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="R1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="op_relacional"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("R1")
					self.cola_gram.encolar("U")
					self.cola_gram.encolar("<")
					#Hemos llegado a <, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","Coma","PuntoYComa","op_logico"]):
					#lamda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="S"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="break"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("break")
					#Hemos llegado a ; , desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("S1")
					self.cola_gram.encolar("id")
					#Hemos llegado a id, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="print"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("print")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="prompt"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("(")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("prompt")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="prompt"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(";")
					self.cola_gram.encolar("X")
					self.cola_gram.encolar("return")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="S1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="op_asignacion" and self.cola_tokens.mostrarPrimero().getExtra()=="&="):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("&=")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="op_asignacion" and self.cola_tokens.mostrarPrimero().getExtra()=="="):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("=")
					#Hemos llegado a =, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="parentesis_apertura"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("L")
					self.cola_gram.encolar("(")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				else:
					self.error=True;
					print "Error"

			elif(self.cola_gram.mostrarUltimo()=="T"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="bool"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("bool")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="int"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("int")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="string"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("string")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="U"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_apertura","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("U1")
					self.cola_gram.encolar("V")

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="U1"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="op_aritmetico"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("U1")
					self.cola_gram.encolar("V")
					self.cola_gram.encolar("+")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","Coma","PuntoYComa","op_relacional","op_logico"] ):
					#lamda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="V"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId()=="parentesis_apertura"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar(")")
					self.cola_gram.encolar("E")
					self.cola_gram.encolar("(")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="cadena"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("cadena")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="entero"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("entero")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId()=="identificador"):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("V1")
					self.cola_gram.encolar("identificador")
					#Hemos llegado a print, desencolamos
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

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
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()

				elif(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","op_aritmetico","Coma","PuntoYComa","op_relacional","op_logico"]):
					#lamda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;

			elif(self.cola_gram.mostrarUltimo()=="X"):
				print "he pasado por " + self.cola_gram.mostrarUltimo()
				if(self.cola_tokens.mostrarPrimero().getId() in ["parentesis_cierre","cadena","entero","identificador"]):
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("E")

				elif(self.cola_tokens.mostrarPrimero().getId()=="PuntoYComa"):
					#lamda
					self.cola_gram.desencolarUltimo()

				else:
					print "Error"
					self.error=True;
			elif(self.cola_gram.mostrarUltimo() in self.terminales):

				print "he pasado por " + self.cola_gram.mostrarUltimo()

				self.cola_tokens.desencolarPrimero()
				self.cola_gram.desencolarUltimo()















				































					
					
					
					
					
					
					
					






					





					







				
	


					




		









