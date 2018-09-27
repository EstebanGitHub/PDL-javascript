class Token:
	id=''
	extra=None
	#extra dependera del tipo de informacion extra que le demos al Token
	
	def __init__(self,id,extra):
		self.id=id
		if type(extra) is int:
			self.value=extra
		elif type(extra) is str:
			self.inf=extra
		elif extra=="__":
			self.extra="__"
	
	def getId(self):
		return self.id
		
	def setId(self,id):
		self.id=id
		
	def getExtra(self):
		return extra
		
	def setExtra(self,id):
		if type(extra) is int:
			self.value=extra
		elif type(extra) is str:
			self.inf=extra
		elif extra=="__":
			self.extra="__"

	def imprimirToken(self):
		print ('<'+self.getId+','+str(self.getExtra)+'>')