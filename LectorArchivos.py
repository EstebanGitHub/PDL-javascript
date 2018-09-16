class LectorArchivos:
	
	posicion=0
	archivo=None

	def __init__ (self,archivo):

		self.archivo=open(archivo,"r")

	def leerLinea(self):
		return self.archivo.readline()

	def leerCaracter(self,linea):
			posicion_aux=self.posicion
			self.posicion=self.posicion+1
			return linea[posicion_aux]
		

			
			
	

