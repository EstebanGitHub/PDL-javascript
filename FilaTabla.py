class FilaTabla:
	tipo=""
	posicion=0
	def __init__(self,tipo,posicion):
		self.tipo=tipo
		self.posicion=posicion
	
	def getTipo(self):
		return self.tipo
	
	def setTipo(self, tipo):
		self.tipo=tipo
		
	def getPosicion(self):
		return self.posicion
	
	def setPosicion(self, posicion):
		self.posicion=posicion
			
	