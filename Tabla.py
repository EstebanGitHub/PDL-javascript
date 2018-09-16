from FilaTabla import FilaTabla


class Tabla:
	listaFilas=[]
	
	def insertarFila(self,FilaTabla):
		self.listaFilas.append(FilaTabla)
	
	def eliminarFila(self,FilaTabla):
		self.listaFilas.remove(FilaTabla)
		
	def buscarEnTabla(self,FilaTabla):
		if FilaTabla in self.listaFilas:
			return true
		else:
			return false
			
	
	