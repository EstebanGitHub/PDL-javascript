from Cola import Cola
from Token import Token
from Tabla import Tabla
from FilaTabla import FilaTabla
from ALexico import ALexico

class ASintactico:
	
	cola_tokens=Cola()#Cola de los tokens, vamos a coger la Cola de la que ha generado el Lexico
	cola_gram=Cola()#Cola del estado actual
	


	def __init__(self,cola_tokens):
		self.cola_tokens = cola_tokens
		self.cola_gram.encolar("$") #empezamos con el dolar

	#Tenemos que construir una nueva gramatica que realice el comportamiento de un analizador sintactico, debido a que su gramatica es de tipo 2, tenemos que controlar en todo momento enque situacion estamos
	#Aquí ya tenemos la cola por defecto y ya no tenemos que leer nada
	def recorrido(self): 
		#Lo primero es mirar con que elemento contamos en la cola de tokens
		#Debemos tomar los First y Follows como refernecias para saber como desplazarnos
		if(cola_tokens.estaVacia() and !cola_gram.estaVacia()):
			print "algo va mal"








	#A esperas de mas clases para tener clara la implementacion

