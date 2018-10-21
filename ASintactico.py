from Cola import Cola
from Token import Token
from Tabla import Tabla
from FilaTabla import FilaTabla
from ALexico import ALexico

class ASintactico:
	
	cola_tokens=Cola()
	#Vamos a coger la Cola de la que ha generado el Lexico


	def __init__(self,cola_tokens):
		self.cola_tokens = cola_tokens

	#Tenemos que construir una nueva gramatica que realice el comportamiento de un analizador sintactico. Logicamente, tambien tendra un automata que vamos a seguir

	#A esperas de mas clases para tener clara la implementacion

