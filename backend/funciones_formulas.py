"""
Funciones.

Contiene lo utlizado en las formulas
"""
import math

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

# funcion para redondear cada resultado hacia arriba
def rendondear(numero):
    """
    Devolvera el numero redondeado
    hacia arriba
    """

    resultado = math.ceil(numero)

    return resultado

# funcion para calcular el GET en schofield
def calcular_get_scho(paciente, ger, fd):
    """
    Devuelve el GET calculado
    """
    get = ger * (paciente.fp + paciente.faf + fd - 2)
    return get

# calcular las kcal por % de cada macro
def calcular_kcal_macro(macros_porcentaje, get):
    """
    Calcula que % le toca de las kcal
    totales en cada macro
    """
    kcal_macros = {}

    for macro, porcentaje in macros_porcentaje.items():

        kcal_macros[macro] = (porcentaje * get) / 100

    return kcal_macros

# calcular gramos por dia macros
def calcular_g_macros(kcal_macros):
    """
    Calcula los gramos por dia
    por cada macro
    """
    g_macros = {}

    for macro, kcal in kcal_macros.items():

        if macro == "proteina" or macro == "hidratos_carbono":

            g_macros[macro] = kcal / 4

        else:
             
             g_macros[macro] = kcal / 9

    return g_macros

# calcular gramos por dia por peso macros
def calcular_g_peso(peso, g_macros):
    """
    Calcula los gramos por peso 
    y por dia de cada macro
    """

    g_peso_macros = {}

    for macro, gramos in g_macros.items():

        g_peso_macros[macro] = gramos / peso
    
    
    return g_peso_macros

# calculo IMC
def calcular_imc(paciente):
    """
    Calcula el imc y retorna
    el resultado
    """

    imc = paciente.peso / paciente.altura ** 2

    return imc

# clasificar el imc
def clasificar_imc(paciente, imc):
    """
    Calculara el su estado
    segun el imc y edad, retornando
    el estado del paciente
    """
    
    # adulto joven
    if 18 <= paciente.edad <= 64:
        
        # verificar imc
        if 18.5 <= imc <= 24.9:
            return "peso normal"
        
        elif 25 <= imc <= 29.9:
            return "sobre peso"
        
        elif 30 <= imc <= 39.9:
            return "obesidad"
        
        elif imc >= 40:
            return "obesidad morbida"
        
        else:
           raise ValueError("El paciente no cumple con el IMC para esta fórmula")
    
    # adulto mayor
    elif paciente.edad >= 65:
        
        # verificar imc
        if 23.1 <= imc <= 27.9:
            return "peso normal"
        
        elif 28 <= imc <= 31.9:
            return "sobre peso"

        elif 32 <= imc <= 39.9:
            return "obesidad"
        
        elif imc >= 40:
            return "obesidad morbida"
        
        else:
            raise ValueError("El paciente no cumple con el IMC para esta fórmula")

    else:
        raise ValueError("error, edad no aceptada")

#  clasificar factorial
def clasificar_factorial(paciente, clasificacion):
    """
    Retornara el factor, dependiendo
    su clasificacion y genero
    """
    
    # segmentar segun su clasificacion
    match clasificacion:
        
        case "peso normal":
            
            # mujer 
            if paciente.genero == "mujer":
                factor = 20.7
                return factor
            
            # hombre
            else:
                factor = 23.6
                return factor
        
        case "sobre peso":

            # mujer
            if paciente.genero == "mujer":
                factor = 19.7
                return factor
            
            # hombre
            else:
                factor = 20
                return factor
        
        case "obesidad":

            # mujer
            if paciente.genero == "mujer":
                factor = 18.3
                return factor
            
            # hombre
            else:
                factor = 19
                return factor
        
        case "obesidad morbida":

            # mujer
            if paciente.genero == "mujer":
                factor = 16.2
                return factor
            
            # hombre
            else:
                factor = 17
                return factor
            
