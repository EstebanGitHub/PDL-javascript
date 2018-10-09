from FilaTabla import FilaTabla


class Tabla:
	listaFilas=[]
	tablaPadre=None
	nombre=""
	archivo=""


	def __init__(self,tablaPadre,nombre):
		self.tablaPadre=tablaPadre
		self.nombre=nombre
		#Vamos dejando claro el nombre y espaciamos lo suficiente
		self.archivo=open(nombre+".txt","a")
		self.archivo.write("CONTENIDO DE LA TABLA #" +  nombre + " :" + "\n" + "\n")
		self.archivo.close()



	def insertarFila(self,FilaTabla):
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

	def esGlobal(self):
		if self.getPadre==self:
			return true
		else return false

	def getNombre(self):
		return self.nombre

	def setNombre(self,nombre):
		self.nombre=nombre


	def escrituraTabla(self,FilaTabla):
		archivo.write("*  LEXEMA : '" + FilaTabla.getLexema() +"'" + "\n"
		 + "   ATRIBUTOS :" + "\n"
		 + "   + tipo : '" + FilaTabla.getTipo() + "'" + "\n" +
		  "   + desplazamiento : '" + FilaTabla.getDesp() + "'" + "\n" +
		   "-------------------------------------" )#Formato a revisar





	
	