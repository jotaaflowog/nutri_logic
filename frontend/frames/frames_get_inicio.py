import customtkinter as ctk
from backend.formulas import *
from backend.manejo_errores import *
from backend.pacientes import Paciente

class GetInicioFrame(ctk.CTkFrame):
    def __init__(self, master, cambiar_frame_callback):
        super().__init__(master)
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

        self.label_error = ctk.CTkLabel(self, text="", text_color="red", font=("Segoe UI", 12))
        self.label_error.grid(row=2, column=0, columnspan=2)
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

        # Mostrar según fórmula
        if seleccionada == "Método Factorial":
            self.label_factor.pack(pady=(10, 0))
            self.entry_factor.pack()

        elif seleccionada in ["Schofield Peso", "Schofield Peso y Talla"]:
            self.label_crecimiento.pack(pady=(10, 0))
            self.entry_crecimiento.pack()
            self.label_desnutricion.pack(pady=(10, 0))
            self.entry_desnutricion.pack()
        
        elif seleccionada == "Factorial de Carrasco":
            self.label_sub_formula.pack(pady=(10, 0))
            self.selector_sub_formula.pack()


    def actualizar_subformulas(self, *args):
        subformula = self.selector_sub_formula.get()
        
        # Ocultamos los campos por defecto
        self.label_delta_negativo.pack_forget()
        self.selector_delta_negativo.pack_forget()

        if subformula == "Restricción Calórica":
            self.label_delta_negativo.pack(pady=(10, 0))
            self.selector_delta_negativo.pack()

    def calcular_get(self):
        
        # variables que no tienen error general
        formula = self.selector_formula.get()
        genero = self.genero.get().lower()

       
        try:
            edad = validar_entero(self.entrada_edad.get(), "Edad")
            peso = validar_entero(self.entrada_peso.get(), "Peso")
            altura = validar_flotante(self.entrada_altura.get(), "Altura")
            fp = validar_flotante(self.fp.get(), "Factor Patológico")
            faf = validar_flotante(self.faf.get(), "Factor Actividad Física")

            # comprobar errores en datos formulas
            if formula == "Método Factorial":
                
                factor = validar_flotante(self.entry_factor.get(), "Factor")

            elif formula in ["Schofield Peso", "Schofield Peso y Talla"]:
                
                validar_edad_menor(edad)
                crecimiento = validar_flotante(self.entry_crecimiento.get(), "Crecimiento")
                f_desnutricion = validar_flotante(self.entry_desnutricion.get(), "Factor Desnutrición")

            self.label_error.grid_remove()
        
        except ValueError as e:

            self.label_error.configure(text=str(e))
            self.label_error.grid()
        
        # en caso de ningun error
        else:

            # creacion paciente
            paciente = Paciente(edad, altura, peso, genero, fp, faf)
            
            
            # formula utilizada
            match formula:
                 
                case "Predictiva Get":
                    get = rendondear(predictiva_get(paciente))
                    print(get)
                 
                case  "Harris-Benedit":
                    get = rendondear(harris_benedit(paciente))
                    print(get)
                
                case "Miffin":
                    get = rendondear(mifflin(paciente))
                    print(get)

                case "OMS":
                    get = rendondear(oms(paciente))
                    print(get)

                case "Método Factorial":
                    get = rendondear(metodo_factorial(paciente, factor))
                    print(get)
                
                case "Schofield Peso":
                    get = rendondear(schofield_peso(paciente, crecimiento, f_desnutricion))
                    print(get)
                
                case "Schofield Peso y Talla":
                    get = rendondear(schofield_peso_talla(paciente, crecimiento, f_desnutricion))
                    print(get)

                case "Factorial de Carrasco":
                    
                    #sub_formulas
                    sub_formula = self.selector_sub_formula.get()
                    match sub_formula:

                        case "Mantenimiento":
                            get = rendondear(factorial_carrasco(paciente, "mantenimiento"))
                            print(get)
                        
                        case "Con enfermedad":
                            get = rendondear(factorial_carrasco(paciente, "con enfermedad"))
                            print(get)
                        
                        case "Restricción Calórica": 
                             
                            try:
                                delta_negativo = validar_entero(self.selector_delta_negativo.get(), "Delta Negativo")
                                self.label_error.grid_remove()
                            
                            except ValueError as e:
                                self.label_error.configure(text=str(e))
                                self.label_error.grid()
                            
                            else:
                                get = rendondear(factorial_carrasco(paciente, "restriccion calorica", delta_negativo))
                                print(get)

                            
                


        

        

