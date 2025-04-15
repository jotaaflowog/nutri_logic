"""
Manejo de erroes.

Acá estará la logica detras de cada error
"""

# verifica que la sea un numero
def validar_entero(valor, campo):
    try:
        return int(valor)
    
    except ValueError:
        raise ValueError(f"El campo '{campo}' está incorrecto o vacío.")
    
# verifica que la sea un numero decimal
def validar_flotante(valor, campo):

    try:
        return float(valor)
    
    except ValueError:
        raise ValueError(f"El campo '{campo}' está incorrecto o vacío.")


# validar edad schofield
def validar_edad_menor(edad):

    if edad > 18:
        raise ValueError ("Selecciona una fórmula válida, esta es solo hasta 18 años.")
    
    else:
        pass
 