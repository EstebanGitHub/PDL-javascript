from FilaTabla import FilaTabla


class Tabla:
	listaFilas=[]
	tablaPadre=None

	def __init__(self,tablaPadre):
		self.tablaPadre=tablaPadre

	def insertarFila(self,FilaTabla,):
		self.listaFilas.append(FilaTabla)

	
	def eliminarFila(self,FilaTabla):
		self.listaFilas.remove(FilaTabla)
		
	def buscarEnTabla(self,FilaTabla):
		if FilaTabla in self.listaFilas:
			return true
		else:
			return false
	def getPadre(self):
		return self.tablaPadre

	def setPadre(self,tablaPadre):
		self.tablaPadre=tablaPadre
		


	
	