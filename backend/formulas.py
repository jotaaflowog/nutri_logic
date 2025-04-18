"""
Formulas

Contiene todas las formulas.
"""
from backend.funciones_formulas import *

# lista con todas las formulas
formulas = ["Predictiva Get", 
            "Harris-Benedit",
            "Miffin",
            "OMS",
            "Método Factorial",
            "Schofield Peso",
            "Schofield Peso y Talla",
            "Factorial de Carrasco",
            "FAO-OMS-UNU < 1 año",
            "FAO-OMS-UNU  > 1 año"]

sub_formulas_carrasco = ["Mantenimiento",
                         "Con enfermedad",
                         "Restricción Calórica"]

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

    # validacion genero hombre
    if paciente.genero == "hombre":

        # validacion edades
        if 0 <= edad <= 3:
            ger = 59.48 * paciente.peso - 30.33
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total
    
        elif 4 <= edad <= 10:
            ger = 22.7 * paciente.peso + 505
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total
        
        elif 11 <= edad <= 18:
            ger = 13.4 * paciente.peso + 693
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total
    
    # validacion mujer
    elif paciente.genero == "mujer":
        
        # validacion edades
        if 0 <= edad <= 3:
            ger = 58.29 * paciente.peso - 31.05
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total
    
        elif 4 <= edad <= 10:
            ger = 20.3 * paciente.peso + 486
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total
        
        elif 11 <= edad <= 18:
            ger = 17.7 * paciente.peso + 659
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total

# formula schofield peso talla -> (GER (faf + fp + fd -2)) + crecimiento
def schofield_peso_talla(paciente, crecimiento, f_desnutricion):
    """
    Calcula el get con peso y talla
    """
    edad = paciente.edad
    
    # validacion genero hombre
    if paciente.genero == "hombre":
        
        # validacion edades
        if 0 <= edad <= 3:
            ger = 0.167 * paciente.peso + 1517.4 * paciente.altura - 617.5
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total

        elif 4 <= edad <= 10:
            ger = 19.6 * paciente.peso + 130.3 * paciente.altura + 414.9
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total

        elif 11 <= edad <= 18:
            ger = 16.25 * paciente.peso + 137.2 * paciente.altura + 515.5
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total

    # validacion genero mujer
    elif paciente.genero == "mujer":
        
        # validacion edades
        if 0 <= edad <= 3:
            ger = 16.25 * paciente.peso + 1023.2 * paciente.altura - 413.5
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total

        elif 4 <= edad <= 10:
            ger = 16.97 * paciente.peso + 161.8 * paciente.altura + 371.2
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total

        elif 11 <= edad <= 18:
            ger = 8.365 * paciente.peso + 465 * paciente.altura + 200
            get = calcular_get_scho(paciente, ger, f_desnutricion)
            get_total = get + crecimiento
            return get_total

# formula factorial de carrasco -> devuelve GET listo
def factorial_carrasco(paciente, sub_formula, delta_negativo=1):
    """
    Devolvera el get listo
    """

    imc = calcular_imc(paciente)
    clasificacion = clasificar_imc(paciente, imc)
    factor = clasificar_factorial(paciente, clasificacion)

    # sub formulas
    match sub_formula:

        case "mantenimiento":
            get = factor * paciente.peso * paciente.faf
            return get
        
        case "con enfermedad":
            get = factor * paciente.peso * (paciente.faf + paciente.fp - 1)
            return get
        
        case "restriccion calorica":
            get = (factor * paciente.peso * paciente.faf) - delta_negativo
            return get

# formula fao oms unu 2004 para bebes -> devuelve GET listo
def fao_oms_onu_bebes(paciente, meses, modo_alimentacion):
    """
    Calcula el get a traves del factor
    retornando el get listo
    """
    
    # clasificar mes
    match meses:

        case 1:
            
            # clasificar alimentacion
            match modo_alimentacion:

                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 106
                            return get

                        case "mujer":
                            get = paciente.peso * 99
                            return get
                
                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 122
                            return get

                        case "mujer":
                            get = paciente.peso * 117
                            return get

        case 2:
            
            # clasificar meteodo alimentacion
            match modo_alimentacion:

                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 98
                            return get

                        case "mujer":
                            get = paciente.peso * 95
                            return get
                
                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 110
                            return get

                        case "mujer":
                            get = paciente.peso * 108
                            return get

        case 3:
            
            # clasificar metodo alimentacion
            match modo_alimentacion:

                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 91
                            return get

                        case "mujer":
                            get = paciente.peso * 90
                            return get

                # formula lactea
                case "fla":
                    
                    #clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 100
                            return get


                        case "mujer":
                            get = paciente.peso * 108
                            return get

        case 4:
            
            # clasificar metodo alimentacion
            match modo_alimentacion:
                
                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 79
                            return get

                        case "mujer":
                            get = paciente.peso * 80
                            return get

                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 86
                            return get

                        case "mujer":
                            get = paciente.peso * 89
                            return get

        case 5:
            
            # clasificar metodo alimentacion
            match modo_alimentacion:

                # leche materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 79
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 79
                            return get

                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 85
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 87 
                            return get

        case 6: 
            
            # clasificar metodo alimentacion
            match modo_alimentacion:

                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 78
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 79
                            return get

                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 83
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 85
                            return get

        case 7:
            
            # clasificar metodo alimentacion
            match modo_alimentacion:

                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 76
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 76
                            return get

                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 81
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 81
                            return get

        case 8:
            
            # clasificar metodo alimentacion
            match modo_alimentacion:
                
                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 77
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 76
                            return get

                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 81
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 81
                            return get

        case 9:
            
            # clasificar metodo alimentacion
            match modo_alimentacion:

                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 77
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 76
                            return get

                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 81
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 81
                            return get
        
        # para meses 10 al 12
        case 10 | 11 | 12:
            
            # clasificar metodo alimentacion
            match modo_alimentacion:

                # lactancia materna
                case "lm":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 79
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 77
                            return get

                # formula lactea
                case "fla":
                    
                    # clasificar genero
                    match paciente.genero:

                        case "hombre":
                            get = paciente.peso * 82
                            return get
                        
                        case "mujer":
                            get = paciente.peso * 81
                            return get
                        
# formula fao oms unu 2004 para menores -> devuelve GET listo
def fao_oms_onu_menores(paciente, actividad_fisica):
    """
    Calcula el get segun edad y 
    actividad fisica, devolviendolo
    """

    # diccionario con todos los factores segun edad y genero
    factores = {
        1:{
            "hombre":{
                "af ligera": False,
                "af moderada": 82
                },

            "mujer":{
                "af ligera": False,
                "af moderada": 80
                }
        },

        2:{
            "hombre":{
                "af ligera": False,
                "af moderada": 84
            },

            "mujer":{
                "af ligera": False,
                "af moderada": 81
            }

        },

        3:{
            "hombre":{
                "af ligera": False,
                "af moderada": 80
            },

            "mujer":{
                "af ligera": False,
                "af moderada": 77
            }
        },

        4:{
            "hombre":{
                "af ligera": False,
                "af moderada": 77
            },

            "mujer":{
                "af ligera": False,
                "af moderada": 74
            }
        },

        5:{
            "hombre":{
                "af ligera": False,
                "af moderada": 74
            },

            "mujer":{
                "af ligera": False,
                "af moderada": 72
            }
        },

        6:{
            "hombre":{
                "af ligera": 62,
                "af moderada": 73
            },
            
            "mujer":{
                "af ligera": 59,
                "af moderada": 69
            }
        },

        7:{
            "hombre":{
                "af ligera": 60,
                "af moderada": 71
            },

            "mujer":{
                "af ligera": 57,
                "af moderada": 67
            }
        },

        8:{
            "hombre":{
                "af ligera": 59,
                "af moderada": 69
            },

            "mujer":{
                "af ligera": 54,
                "af moderada": 64
            }
        },

        9:{
            "hombre":{
                "af ligera": 56,
                "af moderada": 67
            },

            "mujer":{
                "af ligera": 52,
                "af moderada": 61
            }
        },

        10:{
            "hombre":{
                "af ligera": 55,
                "af moderada": 65
            },

            "mujer":{
                "af ligera": 49,
                "af moderada": 58
            }
        },

        11:{
            "hombre":
            {
                "af ligera": 53,
                "af moderada": 62
            },

            "mujer":{
                "af ligera": 47,
                "af moderada": 55
            }
        },

        12:{
            "hombre":{
                "af ligera": 51,
                "af moderada": 60
            },
            
            "mujer":{
                "af ligera": 44,
                "af moderada": 52
            }
        },

        13:{
            "hombre":{
                "af ligera": 49,
                "af moderada": 58
            },

            "mujer":{
                "af ligera": 42,
                "af moderada": 49
            }
        },

        14:{
            "hombre":{
                "af ligera": 48,
                "af moderada": 56
            },

            "mujer":{
                "af ligera": 40,
                "af moderada": 47
            }
        },

        15:{
            "hombre":{
                "af ligera": 45,
                "af moderada": 53
            },

            "mujer":{
                "af ligera": 39,
                "af moderada": 45 
            }
        },

        16:{
            "hombre":{
                "af ligera": 44,
                "af moderada": 52
            },

            "mujer":{
                "af ligera": 38,
                "af moderada": 44
            }
        },

        17:{
            "hombre":{
                "af ligera": 43,
                "af moderada": 50
            },

            "mujer":{
                "af ligera": 37,
                "af moderada":44
            }
        }
    }


    # itinerar en factores para tener el indicado
    factor = factores[paciente.edad][paciente.genero][actividad_fisica]

    if not factor:
        print("La edad del paciente es inválida, utiliza otra")
    
    else:
        get = paciente.peso * factor
        return get