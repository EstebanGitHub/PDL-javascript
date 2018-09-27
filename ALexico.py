from LectorArchivos import LectorArchivos
from Tabla import Tabla
from Token import Token
from LectorArchivos import LectorArchivos



class ALexico:
	estados=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]#Pendiente de comprobar el numero real de estados del automata
	estado_actual=0
	tokens=[]
	fichero_leido=None
	linea=None
	caracter=None
	#La Tabla de simbolos se construirá cunado se inserte la primera fila

	def __init__(self,LectorArchivos):
		self.linea=LectorArchivos.leerLinea()
		self.caracter=LectorArchivos.leerCaracter(self.linea)

	def recorrido(self,LectorArchivos):
		limite=len(LectorArchivos.contenido)
		contador=0
		while contador<limite:
			while self.caracter!='\n' and self.caracter!=None :
				#print self.caracter
				#Interactuamos con el caracter actual, utilizamos ord() para obetenr su valor en ASCII
				#De momento, se consideran los espacios y saltos de linea IGNORABLES
				#Caso comentarios
				if(ord(self.caracter)==47 and estado==0):
					#Transicion a estado correspondiente
				#Resto de casos a implementar, a la espera de un automata perfeccionado
				#vamos a por el siguiente en bucle
				self.caracter=LectorArchivos.leerCaracter(self.linea)
			contador=contador+1	
			LectorArchivos.posicion_caracter=0
			if (self.linea!=None):
				self.linea=LectorArchivos.leerLinea()
				self.caracter=LectorArchivos.leerCaracter(self.linea)
		    
		    


