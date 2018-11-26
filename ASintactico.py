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

	


	def __init__(self,cola_tokens, tabla_global, tablas_funciones):
		self.cola_tokens.encolar(cola_tokens.getElementos())
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
		for token in self.cola_tokens.getElementos():#Mide solo una vez?

			if(self.cola_tokens.estaVacia() and self.cola_gram.estaVacia()==False):
				print "algo va mal"
				#Tenemos que pararnos a ver la condicion de parada con $
			#Siguiendo los First y Follows, estudiamos que regla aplicamos para cada situacion
			elif(self.cola_gram.mostrarUltimo()=="A"):

				if(self.cola_tokens.mostrarPrimero().getId()=="parentesis_apertura"):
					#lambda
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()
				
				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra() in ["int" , "bool" , "string"]):

					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("K")
					self.cola_gram.encolar("id")
					self.cola_gram.encolar("T")
					#Insertamos los elementos al reves para respetar el formato de Cola creado para ALexico

				else:
					print "Error"

			elif(self.cola_gram.mostrarUltimo()=="B"):

				if((self.cola_tokens.mostrarPrimero().getId()=="pal_res" and (self.cola_tokens.mostrarPrimero().getExtra() in ["break","print","prompt"])) or self.cola_tokens.mostrarPrimero().getId()=="identificador" ):
					self.cola_tokens.desencolarPrimero()
					self.cola_gram.desencolarUltimo()
					self.cola_gram.encolar("S")

				elif(self.cola_tokens.mostrarPrimero().getId()=="pal_res" and self.cola_tokens.mostrarPrimero().getExtra()=="if"):

					print("luego mas")





				
	


					




		









