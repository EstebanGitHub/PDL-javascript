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
		self.listaFilas=[]
		self.archivo=open(nombre+".txt","a")
		if(tablaPadre==None):
			self.archivo.write("CONTENIDO DE LA TABLA #" +  nombre + " :" + "\n" + "\n")
		else:
			self.archivo.write("TABLA DE LA FUNCION #" +  nombre + " :" + "\n" + "\n") #Pendiente de modificar,una vez perfeccionado el sintactico y semantico
		



	def insertarFila(self,FilaTabla):
		self.listaFilas.append(FilaTabla)

	
	def eliminarFila(self,FilaTabla):
		self.listaFilas.remove(FilaTabla)
		
	def buscarEnTabla(self,FilaTabla):
		lexema=FilaTabla.getLexema()
		encontrado=False
		for fila in self.listaFilas:
			if fila.getLexema()==lexema:
				encontrado= True
		return encontrado

	def situacionLexema(self,FilaTabla):
		lexema=FilaTabla.getLexema()
		posicion=0
		for fila in self.listaFilas:
			if fila.getLexema()==lexema:
				posicion= self.listaFilas.index(fila)
		return posicion


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

	def getFilaTabla(self,posicion):
		return self.listaFilas[posicion]


	def escrituraTabla(self,FilaTabla):#Pendiente de cambio con la informacion actualizada, de momento para testeo para asegurar la construccion correcta en cada paso
		self.archivo.write("\n" +"*  LEXEMA : '" + FilaTabla.getLexema() +"'" + "\n"
		 + "   ATRIBUTOS :" + "\n"
		 + "   + tipo : '" + FilaTabla.getTipo() + "'" + "\n" +
		  "   + desplazamiento : '" + str(FilaTabla.getDesp()) + "'" + "\n" +
		   "-------------------------------------" )#Formato a priori correcto
	#para apoyo
	def escrituraTablaArgumentos(self,FilaTabla,numero_parametros,parametro_actual,tipo_retorno,nombre_tabla):#para escribir en la tabla global el contenido de una funcion
		if(numero_parametros==0 and parametro_actual==0):#funcion sin parametros
			self.archivo.write("\n" +"*  LEXEMA : '" + nombre_tabla +"'" + "\n"
		 	+ "   ATRIBUTOS :" + "\n"
		 	+ "   + tipo : 'funcion' " + "\n" +
		 	"     + numParam= 0")

		elif(parametro_actual==1):#Solo debemos definir el tipo una vez
			self.archivo.write("\n" +"*  LEXEMA : '" + nombre_tabla +"'" + "\n"
		 	+ "   ATRIBUTOS :" + "\n"
		 	+ "   + tipo : 'funcion' " + "\n" +
		 	"     + numParam= " + str(numero_parametros)+ "\n"
		 	"        + TipoParam" + str(parametro_actual) + ":   '" + str(FilaTabla.getTipo()) +"'"
		 	)


		else:#en caso de varios paramnetros
			self.archivo.write("\n" +
			"        + TipoParam" + str(parametro_actual) + ":   '" + str(FilaTabla.getTipo()) +"'")

		if(numero_parametros==parametro_actual): #cierre
			self.archivo.write("\n" + "           + TipoRetorno:" + str(tipo_retorno) + 
			"\n" +  "-------------------------------------" )




	def mostrarTabla(self):
		for val in self.listaFilas:
			print val.getLexema()
		print self.listaFilas




	
	