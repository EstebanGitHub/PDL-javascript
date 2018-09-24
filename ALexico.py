from LectorArchivos import LectorArchivos
from Tabla import Tabla
from Token import Token
from LectorArchivos import LectorArchivos



class ALexico:
	estados=[0]
	tokens=[]
	fichero_leido=None
	linea=None
	caracter=None

	def __init__(self,LectorArchivos):
		self.linea=LectorArchivos.leerLinea()
		self.caracter=LectorArchivos.leerCaracter(self.linea)

	def recorrido(self,LectorArchivos):
		limite=len(LectorArchivos.contenido)
		contador=0
		while contador<limite:
		    while self.caracter!='\n':
			    print self.caracter
			    #Por aqui tendremos que ir trasteando con los tokens
				if contador<limite-1:
					self.caracter=LectorArchivos.leerCaracter(self.linea) #problema al leer el fin
			    
		    self.linea=LectorArchivos.leerLinea()
		    contador=contador+1	
		    LectorArchivos.posicion_caracter=0;
		    if self.linea !="":
		    	self.caracter=LectorArchivos.leerCaracter(self.linea)
		    
		    


