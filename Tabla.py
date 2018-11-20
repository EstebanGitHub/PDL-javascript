from FilaTabla import FilaTabla


class Tabla:
	listaFilas=[] #debemos identificar cada elemento con su lexema
	tablaPadre=None
	nombre=""
	archivo=""


	def __init__(self,tablaPadre,nombre):
		self.tablaPadre=tablaPadre
		self.nombre=nombre
		#Vamos dejando claro el nombre y espaciamos lo suficiente
		self.archivo=open(nombre+".txt","a")
		if(tablaPadre==None):
			self.archivo.write("CONTENIDO DE LA TABLA #" +  nombre + " :" + "\n" + "\n")
		else:
			self.archivo.write("TABLA DE LA FUNCION #" +  nombre + " :" + "\n" + "\n") #Pendiente de modificar,una vez perfeccionado el sintactico
		



	def insertarFila(self,FilaTabla):
		self.listaFilas.append(FilaTabla)

	
	def eliminarFila(self,FilaTabla):
		self.listaFilas.remove(FilaTabla)
		
	def buscarEnTabla(self,FilaTabla):
		encontrado=False
		if FilaTabla in self.listaFilas:
			return True
		else:
			return False
	def getPadre(self):
		return self.tablaPadre

	def setPadre(self,tablaPadre):
		self.tablaPadre=tablaPadre

	def esGlobal(self):
		if self.getPadre==None:
			return True
		else:
			return False

	def getNombre(self):
		return self.nombre

	def setNombre(self,nombre):
		self.nombre=nombre

	def posicionEnTabla(self,FilaTabla):
		print self.listaFilas #De apoyo, para testeos
		print self.listaFilas.index(FilaTabla) #De apoyo, para testeos
		return self.listaFilas.index(FilaTabla)

	def escrituraTabla(self,FilaTabla):#Pendiente de cambio con la informacion actualizada, de momento para testeo para asegurar la construccion correcta en cada paso
		self.archivo.write("\n" +"*  LEXEMA : '" + FilaTabla.getLexema() +"'" + "\n"
		 + "   ATRIBUTOS :" + "\n"
		 + "   + tipo : '" + FilaTabla.getTipo() + "'" + "\n" +
		  "   + desplazamiento : '" + str(FilaTabla.getDesp()) + "'" + "\n" +
		   "-------------------------------------" )#Formato a priori correcto
	#para apoyo

	def mostrarTabla(self):
		for val in self.listaFilas:
			print val.getLexema()
		print self.listaFilas




	
	