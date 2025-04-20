"""
Manejo de erroes.

Acá estará la logica detras de cada error
"""
import customtkinter as ctk

# verifica que la sea un numero
def validar_entero(valor, campo):

    # comprueba si el campo esta deshabilitado
    if valor.cget("state") == "disabled":
        pass

    else:
        try:
            numero = int(valor.get())

            if numero <= 0:
                raise ValueError
                
            else:
                return numero
        
        except ValueError:
            raise ValueError(f"El campo '{campo}' está incorrecto o vacío.")
    
# verifica que la sea un numero decimal
def validar_flotante(valor, campo):

    # comprueba si el campo esta deshabilitado
    if valor.cget("state") == "disabled":
        pass
    
    else:
        try:
            numero =  float(valor.get())

            if numero <= 0:
                raise ValueError

            else:
                return numero
        
        except ValueError:
            raise ValueError(f"El campo '{campo}' está incorrecto o vacío.")


# validar edad schofield
def validar_edad_menor(edad):

    if edad > 18:
        raise ValueError ("Selecciona una fórmula válida, esta es solo hasta 18 años.")
    
    else:
        pass
 
 # desactivar campos

# deshabilitar campos
def deshabilitar_campos(campos):
    """
    desabilitará los campos que no se 
    utilizan en x formula
    """

    for campo in campos:

        if isinstance(campo, ctk.CTkOptionMenu):
            campo.configure(state="disabled",
                            fg_color="#E0E0E0",
                            text_color="gray",
                            button_color="#CCCCCC",
                            button_hover_color="#BBBBBB")
        
        else:
            campo.configure(state="disabled", fg_color="#E0E0E0", text_color="gray")

# habilitar campos
def habilitar_campos(campos):
    """
    habilitara los campos que se
    usan en x formula
    """

    for campo in campos:

        if isinstance(campo, ctk.CTkOptionMenu):
            campo.configure(state="normal",
                            fg_color="#6A0DAD",
                            text_color="white",
                            button_color="#5a089e",
                            button_hover_color="#4a027e")

        else:
            campo.configure(state="normal", fg_color="white", text_color="black")


