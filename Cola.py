
class Cola:

	elementos=[]

	def __init__(self):
		self.elementos=[]

	def encolar(self,elemento):
		self.elementos.append(elemento)

	def desencolarUltimo(self):
		try:
			return self.elementos.pop()
		except:
			raise ValueError("Esta cola esta vacia")

	def desencolarPrimero(self):
		try:
			return self.elementos.pop(0)
		except:
			raise ValueError("Esta cola esta vacia")

	def estaVacia(self):
		return self.elementos==[]

	def getElementos(self):
		print self.elementos #Pruebas
		return self.elementos

	def mostrarPrimero(self):
		try:
			return self.elementos[0]
		except:
			raise ValueError("Esta cola esta vacia")
	def mostrarUltimo(self):
		try:
			return self.elementos[-1]
		except:
			raise ValueError("Esta cola esta vacia")

	
