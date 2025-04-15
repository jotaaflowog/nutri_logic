"""
Formulas

Contiene todas las formulas.
"""
from funciones_formulas import *

# formula predictiva get -> devuelve GET
def predictiva_get(paciente):
    """
    Fórmula predictiva, devuelve el GET
    :param paciente:
    :return:
    """
    # pasar altura a cm
    altura = altura_en_cm(paciente)

    # validacion de genero mujer
    if paciente.genero == "mujer":

        # validadción edad
        edad = validar_edad(paciente)

        match edad:

            case "menor":
                # validar actividad fisica
                factor = factor_actividad_fisica(paciente)

                match factor:

                    case "inactivo":
                        get = (55.59 - (22.25 * paciente.edad) + (8.43 * altura) + (17.07 * paciente.peso)) * paciente.fp
                        get_total = validar_edad_ninia(paciente, get)
                        return get_total

                    case "poco activo":
                        get = (297.54 - (22.25 * paciente.edad) + (12.77 * altura) + (14.73 * paciente.peso)) * paciente.fp
                        get_total = validar_edad_ninia(paciente, get)
                        return get_total

                    case "activo":
                        get = (189.55 - (22.25 * paciente.edad) + (11.74 * altura) + (18.34 * paciente.peso)) * paciente.fp
                        get_total = validar_edad_ninia(paciente, get)
                        return get_total

                    case "muy activo":
                        get = (709.59 - (22.25 * paciente.edad) + (18.22 * altura) + (14.24 * paciente.peso)) * paciente.fp
                        get_total = validar_edad_ninia(paciente, get)
                        return get_total

            case "mayor":
                # validar actividad fisica
                factor = factor_actividad_fisica(paciente)

                match factor:

                    case "inactivo":
                        get = 584.90 - (7.01 * paciente.edad) + (5.72 * altura) + (11.71 * paciente.peso)
                        return get * paciente.fp

                    case "poco activo":
                        get = 575.77 - (7.01 * paciente.edad) + (6.60 * altura) + (12.14 * paciente.peso)
                        return get * paciente.fp

                    case "activo":
                        get = 710.25 - (7.01 * paciente.edad) + (6.54 * altura) + (12.34 * paciente.peso)
                        return get * paciente.fp

                    case "muy activo":
                        get = 511.83 - (7.01 * paciente.edad) + (9.07 * altura) + (12.56 * paciente.peso)
                        return get * paciente.fp

    # validacion genero hombre
    elif paciente.genero == "hombre":

        # validad edad
        edad = validar_edad(paciente)

        match edad:

            case "menor":

                factor = factor_actividad_fisica(paciente)

                match factor:

                    case "inactivo":
                        get = (447.51 + (3.68 * paciente.edad) + (13.01 * altura) + (13.15 * paciente.peso)) * paciente.fp
                        get_total = validar_edad_ninio(paciente, get)
                        return get_total

                    case "poco activo":
                        get = (19.12 + (3.68 * paciente.edad) + (8.62 * altura) + (20.28 * paciente.peso)) * paciente.fp
                        get_total = validar_edad_ninio(paciente, get)
                        return get_total

                    case "activo":
                        get = (388.19 + (3.68 * paciente.edad) + (12.66 * altura) + (20.46 * paciente.peso)) * paciente.fp
                        get_total = validar_edad_ninio(paciente, get)
                        return get_total

                    case "muy activo":
                        get = (671.75 + (3.68 * paciente.edad) + (15.38 * altura) + (23.25 * paciente.peso)) * paciente.fp
                        get_total = validar_edad_ninio(paciente, get)
                        return get_total

            case "mayor":

                factor = factor_actividad_fisica(paciente)

                match factor:

                    case "inactivo":
                        get = 753.07 - (10.83 * paciente.edad) + (6.50 * altura) + (14.10 * paciente.peso)
                        return get * paciente.fp

                    case "poco activo":
                        get = 581.47 - (10.83 * paciente.edad) + (8.30 * altura) + (14.94 * paciente.peso)
                        return get * paciente.fp

                    case "activo":
                        get = 1004.82 - (10.83 * paciente.edad) + (6.52 * altura) + (15.91 * paciente.peso)
                        return get * paciente.fp

                    case "muy activo":
                        get = 517.88 - (10.83 * paciente.edad) + (15.61 * altura) + (19.11 * paciente.peso)
                        return get * paciente.fp

# formula harris-benedit -> devuelve GET listo -> GER * (faf + fp - 1)
def harris_benedit(paciente):
    """
    formula calculadora, devuelve GER
    :param paciente:
    :return:
    """

    # pasar altura a cm
    altura = altura_en_cm(paciente)

    # validacion mujer
    if paciente.genero == "mujer":
        ger = (paciente.peso * 9.6) + (altura * 1.85) + (paciente.edad * 4.7) + 655
        get = calular_get_total(paciente, ger)
        return get

    elif paciente.genero == "hombre":
        ger = (paciente.peso * 13.8) + (altura * 5.0) - (paciente.edad * 6.8) + 66.5
        get = calular_get_total(paciente, ger)
        return get

# formula mifflin -> devuelve GET listo -> GER * (faf + fp - 1)
def mifflin(paciente):
    """
    Calcula el GET total
    :param paciente:
    :return:
    """

    # pasar altura a cm
    altura =  altura_en_cm(paciente)

    if paciente.genero == "mujer":
        ger = (10 * paciente.peso) + (6.25 * altura) - (5 * paciente.edad) - 161
        get = calular_get_total(paciente, ger)
        return get

    elif paciente.genero == "hombre":
        ger = (10 * paciente.peso) + (6.25 * altura) - (5 * paciente.edad) + 5
        get = calular_get_total(paciente, ger)
        return get

# formula OMS -> devuelve GET listo -> GER * (faf + fp - 1)
def oms(paciente):
    """
    Calcula el GER y devuelve el GET
    """
    
    # validacion de genero mujer
    if paciente.genero == "mujer":
        
        # validacion de generacion
        rango = rango_edad(paciente)

        match rango:

            case "joven":
                ger = (paciente.peso * 14.7) + 496
                get = calular_get_total(paciente, ger)
                return get
            
            case "adulto":
                ger = (paciente.peso * 8.7) + 829
                get = calular_get_total(paciente, ger)
                return get

            case "tercera edad":
                ger = (paciente.peso * 10.5) + 596
                get = calular_get_total(paciente, ger)
                return get
    
    # validacion de genero hombre
    elif paciente.genero == "hombre":
        
        # validacion de generacion
        rango = rango_edad(paciente)

        match rango:

            case "joven":
                ger = (paciente.peso * 15.3) + 679
                get = calular_get_total(paciente, ger)
                return get
            
            case "adulto":
                ger = (paciente.peso * 11.6) + 879
                get = calular_get_total(paciente, ger)
                return get

            case "tercera edad":
                ger = (paciente.peso * 13.5) + 487
                get = calular_get_total(paciente, ger)
                return get

# formula metodo factorial devuelve GET
def metodo_factorial(paciente, factor):
    """
    Calcula el GET total, segun el factor
    """

    get = factor * paciente.peso

    return get

# formula schofield peso devuelve GET listo -> (GER (faf + fp + fd -2)) + crecimiento
def schofield_peso(paciente, crecimiento, f_desnutricion):
    """
    Calculara el get, pero solo con el peso
    """
    edad = paciente.edad

    if paciente.genero == "hombre":

        if 0 <= edad <= 3:
            ger = 59.48 * paciente.peso - 30.33
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get * crecimiento
            return get_total
    
        elif 4 <= edad <= 10:
            ger = 22.7 * paciente.peso + 505
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get * crecimiento
            return get_total
        
        elif 11 <= edad <= 18:
            ger = 13.4 * paciente.peso + 693
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get * crecimiento
            return get_total
    
    elif paciente.genero == "mujer":
        
        if 0 <= edad <= 3:
            ger = 58.29 * paciente.peso - 31.05
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get * crecimiento
            return get_total
    
        elif 4 <= edad <= 10:
            ger = 20.3 * paciente.peso + 486
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get * crecimiento
            return get_total
        
        elif 11 <= edad <= 18:
            ger = 17.7 * paciente.peso + 659
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get * crecimiento
            return get_total

# formula schofield peso talla -> (GER (faf + fp + fd -2)) + crecimiento
def schofield_peso_talla(paciente, crecimiento, f_desnutricion):
    edad = paciente.edad
    pass

