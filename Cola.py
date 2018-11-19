
class Cola:

	elementos=[]

	def __init__(self):
		self.elementos=[]

	def encolar(self,elemento):
		self.elementos.append(elemento)

	def desencolar(self):
		try:
			return self.elementos.pop(0)
		except:
			raise ValueError("Esta cola esta vacia")

	def estaVacia(self):
		return self.elementos==[]

	def getElementos(self):
		print self.elementos #Pruebas


