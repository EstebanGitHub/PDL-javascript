from LectorArchivos import LectorArchivos
from Tabla import Tabla
from Token import Token
from LectorArchivos import LectorArchivos
from ALexico import ALexico


lector_prueba=LectorArchivos("ejemplo2.txt")
prueba=ALexico(lector_prueba)
prueba.recorrido(lector_prueba)#¿Redundante?

