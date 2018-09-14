class Token:
	id=''
	value=0
	inf=''
	
	
	
	#inf o value dependeran del tipo de informacion extra que le demos al Token
	
	def __init__(self,id,extra):
		self.id=id
		if type(extra) is int:
			self.value=extra
		elif type(extra) is str:
			self.inf=extra
	
	def getId(self):
		return self.id
		
	def setID(self,id):
		self.id=id
		
	def getExtra(self):
		return extra
		
	def setExtra(self,id):
		if type(extra) is int:
			self.value=extra
		elif type(extra) is str:
			self.inf=extra
	def imprimirToken(self):
		print ('<'+self.getId+','+str(self.getExtra)+'>')