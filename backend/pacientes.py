"""
Clase paciente.

Contiene lo relacionado con la creación y atributos paciente.
"""


class Paciente():


    # definir los atributos de pacientes
    def __init__(self, edad, altura, peso, genero, fp, faf):
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.fp = fp  # -> factor patológico
        self.faf = faf # -> factor actividad fisica

    def __str__(self):
        texto = f"Edad: {self.edad}\nAltura: {self.altura}\nPeso: {self.peso}\nGenero: {self.genero}\nfaf y fp: {self.faf} {self.fp}"
        return texto
