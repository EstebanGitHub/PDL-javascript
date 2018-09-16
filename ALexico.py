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
		while self.linea!=None:
		    while self.caracter!='\n':
			    print self.caracter
			    self.caracter=LectorArchivos.leerCaracter(self.linea)
		    self.linea=LectorArchivos.leerLinea()
		    


