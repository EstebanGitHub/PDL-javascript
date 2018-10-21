from LectorArchivos import LectorArchivos
from Tabla import Tabla
from Token import Token
from LectorArchivos import LectorArchivos
from ALexico import ALexico
from ASintactico import ASintactico


lector_prueba=LectorArchivos("ejemplo2.txt")
prueba_lex=ALexico(lector_prueba)
prueba_lex.recorrido(lector_prueba)#Redundante?
prueba_sinc=ASintactico(prueba_lex.getCola())#Inicializamos el sintactico con los tokens que tomamos del lexico


