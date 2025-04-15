"""
Pruebas

Contiene las pruebas de cada formula
"""
from backend.formulas import *
from backend.pacientes import Paciente


paciente_prueba = Paciente(21, 1.70, 65, "hombre", 1, 1.1)


resultado = predictiva_get(paciente_prueba)
resultado = rendondear(resultado)
print(resultado)