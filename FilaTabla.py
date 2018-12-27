class FilaTabla:
	lexema=""
	tipo=""
	desplazamiento=0; #Lo obtendremos del Semantico
	dominio=""
	posicion=0
	def __init__(self,lexema,dominio):
		self.lexema=lexema
		self.dominio=dominio
	
	def getTipo(self):
		return self.tipo
	
	def setTipo(self, tipo):
		self.tipo=tipo
		
	def getLexema(self):
		return self.lexema
	
	def setLexema(self, lexema):
		self.lexema=lexema

	def getDominio(self):
		return self.dominio

	def setDominio(self,dominio):
		self.dominio=dominio

	def getDesp(self):
		return self.desplazamiento

	def setDesp(self,desplazamiento):
		self.desplazamiento=desplazamiento

	


	