class Token:
	id=""
	extra=None
	linea=0
	#extra dependera del tipo de informacion extra que le demos al Token
	#linea nos permite tener controlado en cualquier fase del compilador en que linea se encuentra el elemento que estamos trabajando, para el manejo de errores 
	
	def __init__(self,id,extra,linea):
		self.id=id
		if type(extra) is int:
			self.extra=extra
		elif type(extra) is str:
			self.extra=extra
		self.linea=linea
	
	def getId(self):
		return self.id
		
	def setId(self,id):
		self.id=id
		
	def getExtra(self):
		return self.extra
		
	def setExtra(self,extra):
		if type(self.extra) is int:
			self.value=extra
		elif type(self.extra) is str:
			self.extra=extra
		elif extra=="__":
			self.extra="__"

	def getLinea(self):
		return self.linea

	def setLinea(self,linea):
		self.linea=linea

	#Metodo para pruebas, para verlos por consola
	def imprimirToken(self):
		print ("<"+str(self.getId())+","+str(self.getExtra())+">")

	def escribirToken(self):
		archivo=open("tokens_prac.txt","a")
		if (self.extra==""):
			archivo.write("<"+str(self.getId())+",_>"+"\n")
		else:
			archivo.write("<"+str(self.getId())+","+str(self.getExtra())+">"+"\n")
		archivo.close()
