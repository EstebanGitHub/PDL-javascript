class LectorArchivos:
	
	posicion_lineas=0
	posicion_caracter=0
	contenido=[]
	

	def __init__ (self,archivo):

		with open(archivo) as f:
			self.contenido=f.readlines()



	def leerLinea(self):
		posicion_aux=self.posicion_lineas
		self.posicion_lineas=self.posicion_lineas+1
		return self.contenido[posicion_aux]


	def leerCaracter(self,linea):
			posicion_aux=self.posicion_caracter
			self.posicion_caracter=self.posicion_caracter+1
			return linea[posicion_aux]
		

			
			
	

