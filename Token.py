class Token:
	id=""
	extra=None
	#extra dependera del tipo de informacion extra que le demos al Token
	
	def __init__(self,id,extra):
		self.id=id
		if type(extra) is int:
			self.extra=extra
		elif type(extra) is str:
			self.extra=extra
	
	def getId(self):
		return self.id
		
	def setId(self,id):
		self.id=id
		
	def getExtra(self):
		return self.extra
		
	def setExtra(self,id):
		if type(extra) is int:
			self.value=extra
		elif type(extra) is str:
			self.extra=extra
		elif extra=="__":
			self.extra="__"
	#Metodo para pruebas, para verlos por consola
	def imprimirToken(self):
		print ("<"+str(self.getId())+","+str(self.getExtra())+">")

	def escribirToken(self):
		archivo=open("tokens_prac.txt","a")
		archivo.write("<"+str(self.getId())+","+str(self.getExtra())+">"+"\n")
		archivo.close()
