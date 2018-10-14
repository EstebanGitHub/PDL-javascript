from LectorArchivos import LectorArchivos
from Tabla import Tabla
from Token import Token
from LectorArchivos import LectorArchivos
from Cola import Cola
from FilaTabla import FilaTabla



class ALexico:
	palabras_reservadas=["switch","case","if","return","function","break","default","int","string","bool","var","print","prompt"]
	estado_actual=0
	tokens=Cola()
	fichero_leido=None
	linea=None
	caracter=None
	lexema="" #Para guardar en memoria los tokens con mas de un elemento (cadenas, por ejemplo)
	valor=0 #Para guardar en memoria enteros
	reserva_otro_caracter=False
	en_funcion=False
	n_funciones=0

	



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
			while (self.caracter!=None):
				print self.caracter
				#Interactuamos con el caracter actual, utilizamos ord() para obtener su valor en ASCII
				#De momento, se consideran los espacios y saltos de linea IGNORABLES
				#Ojo a los errores

				if(self.estado_actual==0):
					#Caso parentesis de apertura
					if(ord(self.caracter)==40):
						token=Token("parentesis_apertura","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso parentesis cierre
					elif(ord(self.caracter)==41):
						token=Token("parentesis_cierre","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso llave apertura
					elif(ord(self.caracter)==123):
						token=Token("llave_entrada","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso llave cierre
					elif(ord(self.caracter)==125):
						token=Token("llave_salida","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso asignacion
					elif(ord(self.caracter)==61):
						token=Token("op_asignacion","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso suma
					elif(ord(self.caracter)==43):
						token=Token("op_aritmetico","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso operador relacional: <
					elif(ord(self.caracter)==60):
						token=Token("op_relacional","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(tokens)
						

					#Caso dos puntos
					elif(ord(self.caracter)==58):
						token=Token("DosPuntos","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso Punto y Coma
					elif(ord(self.caracter)==59):
						token=Token("PuntoYComa","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso |
					elif(ord(self.caracter)==124):
						self.estado_actual=10

					#Caso coma
					elif(ord(self.caracter)==44):
						token=Token("Coma","")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						

					#Caso &
					elif(ord(self.caracter)==26):
						self.estado_actual=12

					#Caso /
					elif(ord(self.caracter)==47):
						self.estado_actual=15

					#Caso entero
					elif(ord(self.caracter) >= 48 and ord(self.caracter) <= 57):
						self.valor=int(self.caracter)
						self.estado_actual=18

					#Caso cadena
					elif(ord(self.caracter)==39):
						self.estado_actual=20

					#Caso identificador o palabra clave
					elif((ord(self.caracter)>=65 and ord(self.caracter)<=90) or (ord(self.caracter)>=97 and ord(self.caracter)<=122)):
						self.lexema=self.caracter
						self.estado_actual=22

					else:
						pass
						#Mensaje de error, puede que quede algun caracter pendiente


				elif(self.estado_actual==1):
					pass

				elif(self.estado_actual==2):
					pass

				elif(self.estado_actual==3):
					pass

				elif(self.estado_actual==4):
					pass

				elif(self.estado_actual==5):
					pass

				elif(self.estado_actual==6):
					pass

				elif(self.estado_actual==7):
					pass

				elif(self.estado_actual==8):
					pass

				elif(self.estado_actual==9):
					pass

				elif(self.estado_actual==10):
					if(ord(self.caracter)==124):
						token=Token("op_logico","||")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						self.estado_actual=0
						
					else:
						pass
						#Mensaje de error

				elif(self.estado_actual==11):
					pass

				elif(self.estado_actual==12):
					if(self.caracter==61):
						token=Token("op_asignacion","&=")
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						self.estado_actual=0
						
					else:
						pass
						#Mensaje de error


				elif(self.estado_actual==13):
					pass

				elif(self.estado_actual==14):
					pass

				elif(self.estado_actual==15):
					if(ord(self.caracter)==42):
						self.estado_actual=16
					else:
						pass
						#Mensaje de error

				elif(self.estado_actual==16):
					if(ord(self.caracter)==42):
						self.estado_actual=17
					else:
						pass
						#Mantiene el estado 16, no hay errores

				elif(self.estado_actual==17):
					if(ord(self.caracter)==47):
						estado_actual=0
					else:
						estado_actual=16

				elif(self.estado_actual==18):
					if(ord(self.caracter)>=48 and ord(self.caracter)<=57):
						self.valor=self.valor*10 + int(self.caracter)
					else:
						token=Token("entero",self.valor)
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						self.valor=0 #Reiniciamos
						self.estado_actual=0
						self.reserva_otro_caracter=True

						

				elif(self.estado_actual==19):
					pass

				elif(self.estado_actual==20):
					if(ord(self.caracter)==39):
						token=Token("cadena",self.lexema)
						token.imprimirToken()
						token.escribirToken()
						self.tokens.encolar(token)
						self.lexema="" #Reiniciamos
						self.estado_actual=0
						
					else:
						self.lexema=self.lexema + str(self.caracter)


				elif(self.estado_actual==21):
					pass

				elif(self.estado_actual==22):
					if((ord(self.caracter)>=48 and ord(self.caracter)<=57) or ((ord(self.caracter)>=65 and ord(self.caracter)<=90) or (ord(self.caracter)>=97 and ord(self.caracter)<=122)) or ord(self.caracter)==95):
						self.lexema=self.lexema + str(self.caracter)
					elif (self.lexema in self.palabras_reservadas):
						if(self.lexema=="function"):
							#Tenemos que crearle una tabla especial
							tabla_funcion=Tabla(tabla_global,"tabla_funcion " + str(self.n_funciones+1))
							self.n_funciones++
							self.en_funcion=True
							token=Token("pal_res",str(self.lexema))
							token.imprimirToken()
							token.escribirToken()
							self.tokens.encolar(token)
							self.lexema=""#Reiniciamos
							self.estado_actual=0
							self.reserva_otro_caracter=True

							
						else:
							token=Token("pal_res",str(self.lexema))
							token.imprimirToken()
							token.escribirToken()
							self.tokens.encolar(token)
							self.lexema=""#Reiniciamos
							self.estado_actual=0
							self.reserva_otro_caracter=True

					


						
					else:
						fila=FilaTabla(self.lexema,"Global")
						if(tabla_global.buscarEnTabla(fila)):
							token=Token("identificador",tabla_global.posicionEnTabla(fila))
							token.imprimirToken()
							token.escribirToken()
							self.tokens.encolar(token)
							self.estado_actual=0
							self.lexema=""#Reiniciamos
							self.reserva_otro_caracter=True
						else:
							tabla_global.insertarFila(fila)
							tabla_global.escrituraTabla(fila)
							token=Token("identificador",tabla_global.posicionEnTabla(fila))
							token.imprimirToken()
							token.escribirToken()
							self.tokens.encolar(token)
							self.estado_actual=0
							self.lexema=""#Reiniciamos
							self.reserva_otro_caracter=True

							



				#Como vamos un caracter por delante, debemos evitar leer caracteres en los estados finales
				if(self.reserva_otro_caracter==True):
					self.reserva_otro_caracter=False
				else:
					self.caracter=LectorArchivos.leerCaracter(self.linea)

			#Avance
			contador=contador+1	
			LectorArchivos.posicion_caracter=0
			if (self.linea!=None):
				self.linea=LectorArchivos.leerLinea()
				self.caracter=LectorArchivos.leerCaracter(self.linea)

		    
		    


