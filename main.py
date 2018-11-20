from LectorArchivos import LectorArchivos
from Tabla import Tabla
from Token import Token
from LectorArchivos import LectorArchivos
from ALexico import ALexico
from ASintactico import ASintactico


lector_prueba=LectorArchivos("ejemplo2.txt")
#Inicializacion del Lexico
prueba_lex=ALexico(lector_prueba)
prueba_lex.recorrido(lector_prueba)#Redundante?
TablaGlobalCons=prueba_lex.getTablaGlobal()
TablasFuncionesCons=prueba_lex.getTablasFunciones()
#Inicializacion del Sintactico, con la informacion de los tokens y las tablas para actualizarlas con la informacion correspondiente del sintactico
prueba_sinc=ASintactico(prueba_lex.getCola(),TablaGlobalCons,TablasFuncionesCons)
prueba_sinc.recorrido()


