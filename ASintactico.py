from Cola import Cola
from Token import Token
from Tabla import Tabla
from FilaTabla import FilaTabla
from ALexico import ALexico

class ASintactico:
	
	cola_tokens=Cola()#Cola de los tokens, vamos a coger la Cola de la que ha generado el Lexico
	cola_gram=Cola()#Cola del estado actual
	tabla_global=Tabla(None,"TABLA_BASE")#Estado actual de la tabla global, ahora trabajamos con ella
	tablas_funciones=[]
	


	def __init__(self,cola_tokens, tabla_global, tablas_funciones):
		self.cola_tokens = cola_tokens
		self.cola_gram.encolar("$") #empezamos con el dolar
		self.tabla_global=tabla_global
		self.lista_tablas_funciones=tablas_funciones

	#Tenemos que construir una nueva gramatica que realice el comportamiento de un analizador sintactico, debido a que su gramatica es de tipo 2, tenemos que controlar en todo momento enque situacion estamos
	#Aqui ya tenemos la cola por defecto y ya no tenemos que leer nada
	def recorrido(self):
		self.cola_gram.getElementos()
		self.tabla_global.mostrarTabla() 
		#Lo primero es mirar con que elemento contamos en la cola de tokens
		#Debemos tomar los First y Follows como referenecias para saber como desplazarnos
		if(self.cola_tokens.estaVacia() and self.cola_gram.estaVacia()==False):
			print "algo va mal"
		#Siguiendo los First y Follows, estudaiamos que regla aplicamos para cada situacion

		







	#A esperas de mas clases para tener clara la implementacion

