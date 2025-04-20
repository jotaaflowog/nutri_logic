import customtkinter as ctk
from backend.formulas import *
from backend.manejo_errores import *
from backend.pacientes import Paciente

class GetInicioFrame(ctk.CTkFrame):
    def __init__(self, master, cambiar_frame_callback):
        super().__init__(master)
        self.cambiar_frame_callback = cambiar_frame_callback
        self.configure(fg_color="#F9F9FB")
        self.grid_columnconfigure((0, 1), weight=1)

        # ------ Sección Izquierda: Datos del paciente ------
        panel_izq = ctk.CTkFrame(self, fg_color="transparent")
        panel_izq.grid(row=0, column=0, padx=40, pady=20, sticky="n")

        ctk.CTkLabel(panel_izq,
                     text="🩺 Datos del Paciente",
                     font=("Segoe UI", 16, "bold"),
                     text_color="#6A0DAD").pack(pady=(0, 20))

        ctk.CTkLabel(panel_izq, text="Edad (años)").pack(anchor="w")
        self.entrada_edad = ctk.CTkEntry(panel_izq, width=200)
        self.entrada_edad.pack(pady=(0, 10))

        ctk.CTkLabel(panel_izq, text="Altura (m)").pack(anchor="w")
        self.entrada_altura = ctk.CTkEntry(panel_izq, width=200)
        self.entrada_altura.pack(pady=(0, 10))

        ctk.CTkLabel(panel_izq, text="Peso (kg)").pack(anchor="w")
        self.entrada_peso = ctk.CTkEntry(panel_izq, width=200)
        self.entrada_peso.pack(pady=(0, 10))

        ctk.CTkLabel(panel_izq, text="Género").pack(anchor="w")
        self.genero = ctk.CTkOptionMenu(panel_izq,
                                        values=["Hombre", "Mujer"],
                                        width=200,
                                        height=35,
                                        fg_color="#6A0DAD",
                                        text_color="white",
                                        button_color="#5a089e",
                                        button_hover_color="#4a027e",
                                        corner_radius=10)
        self.genero.pack(pady=(0, 10))

        ctk.CTkLabel(panel_izq, text="Factor Patológico").pack(anchor="w")
        self.fp = ctk.CTkEntry(panel_izq, width=200)
        self.fp.pack(pady=(0, 10))

        ctk.CTkLabel(panel_izq, text="Factor Actividad Física").pack(anchor="w")
        self.faf = ctk.CTkEntry(panel_izq, width=200)
        self.faf.pack(pady=(0, 10))

        # ------ Sección Derecha: Selector de fórmula ------
        panel_der = ctk.CTkFrame(self, fg_color="transparent")
        panel_der.grid(row=0, column=1, padx=40, pady=20, sticky="n")

        ctk.CTkLabel(panel_der,
                     text="Selecciona fórmula",
                     font=("Segoe UI", 13, "bold"),
                     text_color="#6A0DAD").pack(pady=(0, 10))

        self.selector_formula = ctk.CTkOptionMenu(panel_der,
                                                  values=formulas,
                                                  command=self.actualizar_campos_extras,
                                                  width=240,
                                                  height=35,
                                                  fg_color="#6A0DAD",
                                                  button_color="#5a089e",
                                                  text_color="white",
                                                  dropdown_fg_color="white",
                                                  dropdown_hover_color="#d6c1e8",
                                                  dropdown_text_color="#333")
        self.selector_formula.pack()

        # ------ Campos adicionales (ocultos por defecto) ------
        self.label_factor = ctk.CTkLabel(panel_der, text="Factor:")
        self.entry_factor = ctk.CTkEntry(panel_der)

        self.label_crecimiento = ctk.CTkLabel(panel_der, text="Crecimiento:")
        self.entry_crecimiento = ctk.CTkEntry(panel_der)

        self.label_desnutricion = ctk.CTkLabel(panel_der, text="Factor Desnutrición:")
        self.entry_desnutricion = ctk.CTkEntry(panel_der)

        self.label_sub_formula = ctk.CTkLabel(panel_der, text="Sub Fórmula:")
        self.selector_sub_formula = ctk.CTkOptionMenu(panel_der,
                                                        values=sub_formulas_carrasco,
                                                        command=self.actualizar_subformulas,
                                                        width=240,
                                                        height=35,
                                                        fg_color="#6A0DAD",
                                                        button_color="#5a089e",
                                                        text_color="white",
                                                        dropdown_fg_color="white",
                                                        dropdown_hover_color="#d6c1e8",
                                                        dropdown_text_color="#333")
        
        self.label_delta_negativo = ctk.CTkLabel(panel_der, text="Delta Negativo:")
        self.selector_delta_negativo = ctk.CTkEntry(panel_der)

        self.label_meses = ctk.CTkLabel(panel_der, text="Meses:")
        self.entry_meses = ctk.CTkEntry(panel_der)


        self.label_modo_alimentacion = ctk.CTkLabel(panel_der, text="Método Alimentación")
        self.selector_modo_alimentacion = ctk.CTkOptionMenu(panel_der,
                                                        values=["LM", "FLA"],
                                                        width=240,
                                                        height=35,
                                                        fg_color="#6A0DAD",
                                                        button_color="#5a089e",
                                                        text_color="white",
                                                        dropdown_fg_color="white",
                                                        dropdown_hover_color="#d6c1e8",
                                                        dropdown_text_color="#333")
        

        self.label_actividad_fisica = ctk.CTkLabel(panel_der, text="Nivel Actividad Física")
        self.selector_actividad_fisica = ctk.CTkOptionMenu(panel_der,
                                                        values=["AF Ligera", "AF Moderada"],
                                                        width=240,
                                                        height=35,
                                                        fg_color="#6A0DAD",
                                                        button_color="#5a089e",
                                                        text_color="white",
                                                        dropdown_fg_color="white",
                                                        dropdown_hover_color="#d6c1e8",
                                                        dropdown_text_color="#333")

        # ------ Botón Calcular ------
        btn_calcular = ctk.CTkButton(self,
                                     text="Calcular",
                                     font=("Segoe UI", 14),
                                     width=200,
                                     height=45,
                                     corner_radius=14,
                                     fg_color="#6A0DAD",
                                     hover_color="#5a089e",
                                     text_color="white",
                                     command=self.calcular_get)
        btn_calcular.grid(row=1, column=0, columnspan=2, pady=(20, 10))

       
        # Frame inferior que contiene botón y mensaje de error
        frame_inferior = ctk.CTkFrame(self, fg_color="transparent")
        frame_inferior.grid(row=99, column=0, columnspan=2, sticky="sew", padx=20, pady=(0, 20))

        # Configurar columnas del frame_inferior
        frame_inferior.grid_columnconfigure(0, weight=0)  # Botón izquierda
        frame_inferior.grid_columnconfigure(1, weight=1)  # Espacio expansivo
        frame_inferior.grid_columnconfigure(2, weight=0)  # Label de error

        # Botón alineado a la izquierda
        self.btn_volver_inicio = ctk.CTkButton(
            frame_inferior,
            text="← Volver al inicio",
            width=180,
            fg_color="#6A0DAD",
            text_color="white",
            corner_radius=14,
            command= self.volver_inicio
        )
        self.btn_volver_inicio.grid(row=0, column=0, sticky="w")

        # Label de error con alineación visual centrada respecto al ancho de la ventana
        self.label_error = ctk.CTkLabel(
            frame_inferior,
            text="",
            text_color="red",
            font=("Segoe UI", 12)
        )
        self.label_error.grid(row=0, column=2, sticky="", padx=(0, 272)) 
        self.label_error.grid_remove()



    def actualizar_campos_extras(self, seleccionada):
        # Ocultar todos
        self.label_factor.pack_forget()
        self.entry_factor.pack_forget()
        self.label_crecimiento.pack_forget()
        self.entry_crecimiento.pack_forget()
        self.label_desnutricion.pack_forget()
        self.entry_desnutricion.pack_forget()
        self.label_sub_formula.pack_forget()
        self.selector_sub_formula.pack_forget()
        self.label_delta_negativo.pack_forget()
        self.selector_delta_negativo.pack_forget()
        self.label_meses.pack_forget()
        self.entry_meses.pack_forget()
        self.label_modo_alimentacion.pack_forget()
        self.selector_modo_alimentacion.pack_forget()
        self.label_actividad_fisica.pack_forget()
        self.selector_actividad_fisica.pack_forget()

        # habilitar o desabilitar campos por formula
        if seleccionada == "Predictiva Get":

            # campos para activar
            campos_activar = [
                self.entrada_edad,
                self.entrada_altura,
                self.entrada_peso,
                self.genero,
                self.fp,
                self.faf
                
            ]
            habilitar_campos(campos_activar)
        
        elif seleccionada == "Harris-Benedit":
            
            # campos para activar
            campos_activar = [
                self.entrada_edad,
                self.entrada_altura,
                self.entrada_peso,
                self.genero,
                self.fp,
                self.faf
            ]

            habilitar_campos(campos_activar)
        
        elif seleccionada == "Mifflin":
            
            # campos para activar
            campos_activar = [
                self.entrada_edad,
                self.entrada_altura,
                self.entrada_peso,
                self.genero,
                self.fp,
                self.faf
            ]

            habilitar_campos(campos_activar)
        
        elif seleccionada == "OMS":

            # campos para activar
            campos_activar = [
                self.entrada_edad,
                self.entrada_peso,
                self.genero,
                self.fp,
                self.faf
            ]

            habilitar_campos(campos_activar)

            # campos para deshabilitar
            campos_desactivar = [
                self.entrada_altura
            ]

            deshabilitar_campos(campos_desactivar)

        elif seleccionada == "Método Factorial":

            # campos para activar
            campos_activar = [
                self.entrada_peso
            ]

            habilitar_campos(campos_activar)

            # campos para desactivar
            campos_desactivar = [
                self.entrada_edad,
                self.entrada_altura,
                self.genero,
                self.fp,
                self.faf
            ]

            deshabilitar_campos(campos_desactivar)
            
            # campos exclusivos de formula
            self.label_factor.pack(pady=(10, 0))
            self.entry_factor.pack()

        elif seleccionada in ["Schofield Peso", "Schofield Peso y Talla"]:

            # campos para activar en comun
            campos_activar = [
                self.entrada_edad,
                self.entrada_peso,
                self.genero,
                self.fp,
                self.faf
            ]

            habilitar_campos(campos_activar)

            # habilitar o desactivar campo segun cual sea
            match seleccionada:
                
                case "Schofield Peso":
                    # desactivar campo
                    campos_desactivar = [self.entrada_altura]
                    deshabilitar_campos(campos_desactivar)

                case _:
                    # activar campo
                    campos_activar = [self.entrada_altura]
                    habilitar_campos(campos_activar)

            # campos exclusivos de formula
            self.label_crecimiento.pack(pady=(10, 0))
            self.entry_crecimiento.pack()
            self.label_desnutricion.pack(pady=(10, 0))
            self.entry_desnutricion.pack()
        
        elif seleccionada == "Factorial de Carrasco":
            
            # campos para activar
            campos_activar = [
                self.entrada_edad,
                self.entrada_altura,
                self.entrada_peso,
                self.genero,
                self.faf
            ]
            habilitar_campos(campos_activar)

            # campos exclusivos de formula
            self.label_sub_formula.pack(pady=(10, 0))
            self.selector_sub_formula.pack()
        
        elif seleccionada == "FAO-OMS-UNU < 1 año":

            # campos para activar
            campos_activar = [
                self.entrada_peso,
                self.genero
            ]
            habilitar_campos(campos_activar)

            # campos para desactivar
            campos_desactivar = [
                self.entrada_edad,
                self.entrada_altura,
                self.fp,
                self.faf
            ]
            deshabilitar_campos(campos_desactivar)

            # campos exclusivos de la formula
            self.label_meses.pack(pady=(10, 0))
            self.entry_meses.pack(pady=(10, 0))
            self.label_modo_alimentacion.pack(pady=(10, 0))
            self.selector_modo_alimentacion.pack()
        

        elif seleccionada == "FAO-OMS-UNU  > 1 año":

            # campos para activar
            campos_activar = [
                self.entrada_edad,
                self.entrada_peso,
                self.genero
            ]
            habilitar_campos(campos_activar)

            # campos para desactivar
            campos_desactivar = [
                self.fp,
                self.faf
            ]
            deshabilitar_campos(campos_desactivar)

            # campos exclusivos de la formula
            self.label_actividad_fisica.pack(pady=(10, 0))
            self.selector_actividad_fisica.pack()


    def actualizar_subformulas(self, *args):
        subformula = self.selector_sub_formula.get()
        
        # Ocultamos los campos por defecto
        self.label_delta_negativo.pack_forget()
        self.selector_delta_negativo.pack_forget()

        if subformula == "Restricción Calórica":

            # deshabilitar campo
            deshabilitar_campos([self.fp])

            self.label_delta_negativo.pack(pady=(10, 0))
            self.selector_delta_negativo.pack()
        
        elif subformula == "Con enfermedad":
            # habilitar campo
            habilitar_campos([self.fp])
        
        else:
            # deshabilitar campo
            deshabilitar_campos([self.fp])


    def calcular_get(self):
        
        # variables que no tienen error general
        formula = self.selector_formula.get()
        genero = self.genero.get().lower()

       
        try:
            edad = validar_entero(self.entrada_edad, "Edad")
            peso = validar_entero(self.entrada_peso, "Peso")
            altura = validar_flotante(self.entrada_altura, "Altura")
            fp = validar_flotante(self.fp, "Factor Patológico")
            faf = validar_flotante(self.faf, "Factor Actividad Física")

            # creacion paciente
            paciente = Paciente(edad, altura, peso, genero, fp, faf)

            # comprobar errores en datos formulas
            if formula == "Predictiva Get":
                 if edad <= 2:
                    raise ValueError("El paciente tiene que ser mayor a 2 años para Predictiva GET")
            
            elif formula == "OMS":
                if edad <= 17:
                    raise ValueError(f"La edad mímina para {formula} es de 18 años")

            elif formula == "Método Factorial":
            
                factor = validar_flotante(self.entry_factor, "Factor")

            elif formula in ["Schofield Peso", "Schofield Peso y Talla"]:
                
                validar_edad_menor(edad)
                crecimiento = validar_flotante(self.entry_crecimiento, "Crecimiento")
                f_desnutricion = validar_flotante(self.entry_desnutricion, "Factor Desnutrición")
            
            elif formula == "Factorial de Carrasco":
                
                if edad <= 17:
                    raise ValueError(f"La edad mímina para {formula} es de 18 años")
                
                imc = calcular_imc(paciente)
                clasificar = clasificar_imc(paciente, imc)
                
                #sub_formulas
                sub_formula = self.selector_sub_formula.get()

                if sub_formula == "Restricción Calórica":
                    delta_negativo = validar_entero(self.selector_delta_negativo, "Delta Negativo")

            elif formula == "FAO-OMS-UNU < 1 año":
                meses = validar_entero(self.entry_meses, "Meses")

                if meses > 12:
                    raise ValueError("Solo pueden ser hasta 12 meses")

            elif formula == "FAO-OMS-UNU  > 1 año":
                nivel_actividad_fisica = self.selector_actividad_fisica.get().lower()
                

                if edad > 17:
                    raise ValueError ('La edad "máxima para FAO-OMS-UNU  > 1 año" es de 17 años.')
                
                elif nivel_actividad_fisica == "af ligera" and 1 <= edad <= 5:
                    raise ValueError ("Para usar AF ligera, la edad mínima es de 6 años.")
                

            self.label_error.grid_remove()
        
        except ValueError as e:

            self.label_error.configure(text=str(e))
            self.label_error.grid()
        
        # en caso de ningun error
        else:
            
            
            # formula utilizada
            match formula:
                 
                case "Predictiva Get":
                    get = rendondear(predictiva_get(paciente))
                    
                 
                case  "Harris-Benedit":
                    get = rendondear(harris_benedit(paciente))
                    
                
                case "Mifflin":
                    get = rendondear(mifflin(paciente))
                    

                case "OMS":
                    get = rendondear(oms(paciente))
                    

                case "Método Factorial":
                    get = rendondear(metodo_factorial(paciente, factor))
                    
                
                case "Schofield Peso":
                    get = rendondear(schofield_peso(paciente, crecimiento, f_desnutricion))
                    
                
                case "Schofield Peso y Talla":
                    get = rendondear(schofield_peso_talla(paciente, crecimiento, f_desnutricion))
                    

                case "Factorial de Carrasco":
                    
                    match sub_formula:

                        case "Mantenimiento":
                            get = rendondear(factorial_carrasco(paciente, "mantenimiento"))
                            
                        
                        case "Con enfermedad":
                            get = rendondear(factorial_carrasco(paciente, "con enfermedad"))
                            
                        
                        case "Restricción Calórica": 
                            get = rendondear(factorial_carrasco(paciente, "restriccion calorica", delta_negativo))
                            
                                
                

                case "FAO-OMS-UNU < 1 año":
                    modo_alimentacion = self.selector_modo_alimentacion.get().lower()
                    get = rendondear(fao_oms_onu_bebes(paciente, meses, modo_alimentacion))
                    
                

                case "FAO-OMS-UNU  > 1 año":
                    get = rendondear(fao_oms_onu_menores(paciente, nivel_actividad_fisica))
                    


            # pasar el siguiente frame
            self.cambiar_frame_callback("get_tabla")
            self.master.frames["get_tabla"].set_resultado(get, peso)

    def volver_inicio(self):

        # Limpiar campos de entrada básicos
        self.entrada_edad.delete(0, "end")
        self.entrada_altura.delete(0, "end")
        self.entrada_peso.delete(0, "end")
        self.fp.delete(0, "end")
        self.faf.delete(0, "end")

        # Restaurar el selector de género
        self.genero.set("Hombre")

        # Restaurar la fórmula a la predeterminada
        self.selector_formula.set("Predictiva Get")

        # Limpiar y ocultar campos adicionales
        self.entry_factor.delete(0, "end")
        self.entry_crecimiento.delete(0, "end")
        self.entry_desnutricion.delete(0, "end")
        self.entry_meses.delete(0, "end")
        self.selector_delta_negativo.delete(0, "end")

        self.actualizar_campos_extras("Predictiva Get")

        # Restaurar sub formularios a valor por defecto
        self.selector_sub_formula.set("Mantenimiento")
        self.selector_modo_alimentacion.set("LM")
        self.selector_actividad_fisica.set("AF Ligera")

        # Ocultar errores si hay alguno visible
        self.label_error.configure(text="")
        self.label_error.grid_remove()   

        self.cambiar_frame_callback("inicio")                  
                


        

        

