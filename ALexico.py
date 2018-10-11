from LectorArchivos import LectorArchivos
from Tabla import Tabla
from Token import Token
from LectorArchivos import LectorArchivos
from Cola import Cola



class ALexico:
	palabras_reservadas=["switch","case","if","return","function","break","default","int","string","bool","var","print","prompt"]
	estado_actual=0
	tokens=Cola()
	fichero_leido=None
	linea=None
	caracter=None
	lexema="" #Para guardar en memoria los tokens con mas de un elemento (cadenas, por ejemplo)
	valor=0 #Para guardar en memoria enteros



	def __init__(self,LectorArchivos):
		self.linea=LectorArchivos.leerLinea()
		self.caracter=LectorArchivos.leerCaracter(self.linea)

	def getCola(self):
		return self.tokens

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
				#Ojo a los errores

				
				
				if(estado_actual==0):
					#Caso parentesis de apertura
					if(ord(self.caracter)==40):
						token=Token("parentesis_apertura","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso parentesis cierre
					elif(ord(self.caracter)==41):
						token=Token("parentesis_cierre","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso llave apertura
					elif(ord(self.caracter)==123):
						token=Token("llave_entrada","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso llave cierre
					elif(ord(self,caracter)==125):
						token=Token("llave_salida","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso asignacion
					elif(ord(self.caracter)==61):
						token=Token("op_asignacion","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso suma
					elif(ord(self.caracter)==43):
						token=Token("op_aritmetico","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso operador relacional: <
					elif(ord(self.caracter)==60):
						token=Token("op_relacional","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(tokens)

					#Caso dos puntos
					elif(ord(self.caracter)==58):
						token=Token("DosPuntos","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso Punto y Coma
					elif(ord(self.caracter)==59):
						token=Token("PuntoYComa","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso |
					elif(ord(self.caracter)==124):
						self.estado_actual=10

					#Caso coma
					elif(ord(self.caracter)==44):
						token=Token("Coma","")
						token.imprimirToken()
						token.escribirToken()
						tokens.encolar(token)

					#Caso &
					elif(ord(self.caracter)==26):
						self.estado_actual=12

					#Caso /
					elif(ord(self.caracter)==47):
						self.estado_actual=15

					#Caso entero
					elif(ord(self.caracter) >= 0 and ord(self.caracter) <= 9):
						self.valor=int(self.caracter)
						self.estado_actual=18

					#Caso cadena
					elif(ord(self.caracter)==27):
						self.estado_actual=20

					#Caso identificador o palabra clave
					elif((ord(self.caracter)>=65 and ord(self.caracter)<=90) or (ord(self.caracter)>=97 and ord(self.caracter)<=122)):
						lexema=self.caracter
						self.estado_actual=22





				elif(estado_actual==1):
					pass

				elif(estado_actual==2):

				elif(estado_actual==3):

				elif(estado_actual==4):

				elif(estado_actual==5):

				elif(estado_actual==6):

				elif(estado_actual==7):

				elif(estado_actual==8):

				elif(estado_actual==9):

				elif(estado_actual==10):

				elif(estado_actual==11):

				elif(estado_actual==12):

				elif(estado_actual==13):

				elif(estado_actual==14):

				elif(estado_actual==15):

				elif(estado_actual==16):

				elif(estado_actual==17):

				elif(estado_actual==18):

				elif(estado_actual==19):

				elif(estado_actual==20):

				elif(estado_actual==21):

				elif(estado_actual==22):

				#El resto de tokens a generar dependen de los estados del automata, luego esperaremos a tener el automata en condiciones



				#Aquí debajo vamos a poner la condicion de error, para la cual debe cumplirse que ninguna de las condiciones anterioes del automata se ha cumplido

				self.caracter=LectorArchivos.leerCaracter(self.linea)

			contador=contador+1	
			LectorArchivos.posicion_caracter=0
			if (self.linea!=None):
				self.linea=LectorArchivos.leerLinea()
				self.caracter=LectorArchivos.leerCaracter(self.linea)
		    
		    


