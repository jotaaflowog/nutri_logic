"""
Funciones.

Contiene lo utlizado en las formulas
"""

# funcion para pasar altura a cm
def altura_en_cm(paciente):

    altura_cm = paciente.altura * 100

    return altura_cm

# funcion para definir rango actividad fisica
def factor_actividad_fisica(paciente):

    if 1 <= paciente.faf <= 1.1:
        return "inactivo"

    elif 1.2 <= paciente.faf <= 1.4:
        return "poco activo"

    elif 1.5 <= paciente.faf <= 1.8:
        return "activo"

    elif 1.9 <= paciente.faf <= 2:
        return "muy activo"

# funcion para validar si es menor o mayor de 18
def validar_edad(paciente):
    """
    validará que rango de edad es el
    paciente
    :param paciente:
    :return:
    """

    if 3 <= paciente.edad <= 18:
        return "menor"

    elif paciente.edad > 18:
        return "mayor"

# funcion para sumar al get de la menor
def validar_edad_ninia(paciente, get):
    """
    Validara que rango se encuentra
    la manor
    :param paciente:
    :param get:
    :return:
    """

    if 3 <= paciente.edad <= 8:
        get_total = get + 15
        return get_total

    elif  9 <= paciente.edad <= 13:
        get_total = get + 30
        return get_total

    elif paciente.edad >= 14:
        get_total = get + 20
        return get_total

# funcion para sumar al get del menor
def validar_edad_ninio(paciente, get):
    """
    Validara que rango se encuentra
    el manor
    :param paciente:
    :param get:
    :return:
    """

    if paciente.edad == 3:
        get_total = get + 20
        return get_total

    elif 4 <= paciente.edad <= 8:
        get_total = get + 15
        return get_total

    elif 9 <= paciente.edad <= 13:
        get_total = get + 25
        return get_total

    elif paciente.edad >= 14:
        get_total = get + 20
        return get_total

# funcion para calcular el GET con el GER
def calular_get_total(paciente, ger):

    get = ger * (paciente.faf + paciente.fp - 1)

    return get

# funcion para definir un rango de edad (para OMS)
def rango_edad(paciente):
    """
    Devuelve el rango de edad
    """
    
    edad = paciente.edad

    if 18 <= edad <= 29:
        return "joven"
    
    elif 30 <= edad <= 59:
        return "adulto"
    
    elif edad >= 60:
        return "tercera edad"

