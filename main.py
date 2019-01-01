from LectorArchivos import LectorArchivos
from Tabla import Tabla
from Token import Token
from LectorArchivos import LectorArchivos
from ALexico import ALexico
from ASintactico import ASintactico
from ASemantico import ASemantico
import copy


lector_prueba=LectorArchivos("ejemplosem5.txt")
#Inicializacion del Lexico
prueba_lex=ALexico(lector_prueba)
prueba_lex.recorrido(lector_prueba)#Redundante?
ColaTokens=prueba_lex.getCola()
ColaTokens_copia=copy.deepcopy(ColaTokens)
#Inicializacion del Sintactico, con la informacion de los tokens y las tablas para actualizarlas con la informacion correspondiente del sintactico
prueba_sinc=ASintactico(ColaTokens)
prueba_sinc.recorrido()

prueba_sem=ASemantico(ColaTokens_copia)
prueba_sem.recorrido()

#Y si imprimimos la tabla y los tokens al final?


