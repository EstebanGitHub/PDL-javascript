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
	lexema="" #Para guardar en memoria los tokens con mas de un elemento (cadenas, por ejemplo)

	def __init__(self,LectorArchivos):
		self.linea=LectorArchivos.leerLinea()
		self.caracter=LectorArchivos.leerCaracter(self.linea)

	def recorrido(self,LectorArchivos):
		limite=len(LectorArchivos.contenido)
		contador=0
		tabla_global=Tabla(None,"Tabla Global") #Creamos la tabla global, ya que esta minimo va a estar
		while contador<limite:
			while self.caracter!='\n' and self.caracter!=None :
				print self.caracter
				#Interactuamos con el caracter actual, utilizamos ord() para obtener su valor en ASCII
				#De momento, se consideran los espacios y saltos de linea IGNORABLES
				#A las espera de un automata perfeccionado para definir los estados
				
				#Caso /
				if(ord(self.caracter)==47 and self.estado_actual==0):
					pass

				#Caso *
				if(ord(self.caracter)==42 and self.estado_actual==0):
					pass

				#Caso '
				if(ord(self.caracter)==39 and self.estado_actual==0):	
					pass
			
				#Caso parentesis apertura
				if(ord(self.caracter)==40 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("parentesis_apertura","")
					token.imprimirToken()
					token.escribirToken()

				#Caso parentesis cierre
				if(ord(self.caracter)==41 and self.estado_actual==0):

					token=Token("parentesis_cierre","")
					token.imprimirToken()
					token.escribirToken()

				#Caso llave apertura
				if(ord(self.caracter)==123 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("llave_apertura","")
					token.imprimirToken()
					token.escribirToken()

				#Caso llave cierre
				if(ord(self.caracter)==125 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("llave_cierre","")
					token.imprimirToken()
					token.escribirToken()

				#Caso coma
				if(ord(self.caracter)==44 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("Coma","")
					token.imprimirToken()
					token.escribirToken()

				#Caso dos puntos
				if(ord(self.caracter)==58 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("DosPuntos","")
					token.imprimirToken()
					token.escribirToken()

				#Caso punto y coma
				if(ord(self.caracter)==59 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("PuntoYComa","")
					token.imprimirToken()
					token.escribirToken()

				#Caso operador aritmetico: suma
				if(ord(self.caracter)==43 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("op_aritmetico","+")
					token.imprimirToken()
					token.escribirToken()

				#Caso operador relacional: <
				if(ord(self.caracter)==60 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("op_relacional","<")
					token.imprimirToken()
					token.escribirToken()


				#Caso operador asignacion: =
				if (ord(self.caracter)==61 and self.estado_actual==0):
					#self.estado_actual=1, innecesario ya que vamos a volver a 0
					token=Token("op_asignacion","=")
					token.imprimirToken()
					token.escribirToken()

				#El resto de tokens a generar dependen de los estados del automata, luego esperaremos a tener el automata en condiciones



				#Aquí debajo vamos a poner la condicion de error, para la cual debe cumplirse que ninguna de las condiciones anterioes del automata se ha cumplido

				self.caracter=LectorArchivos.leerCaracter(self.linea)

			contador=contador+1	
			LectorArchivos.posicion_caracter=0
			if (self.linea!=None):
				self.linea=LectorArchivos.leerLinea()
				self.caracter=LectorArchivos.leerCaracter(self.linea)
		    
		    


