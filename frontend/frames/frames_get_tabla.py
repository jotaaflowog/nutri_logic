import customtkinter as ctk
from backend.funciones_formulas import *
from backend.manejo_errores import *

class GetTablaFrame(ctk.CTkFrame):
    def __init__(self, master, cambiar_frame_callback):
        super().__init__(master)
        self.cambiar_frame_callback = cambiar_frame_callback
        self.configure(fg_color="#F9F9FB")

        # configuración general del frame principal
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ===== Panel superior =====
        panel_superior = ctk.CTkFrame(self, fg_color="transparent")
        panel_superior.grid(row=0, column=0, sticky="nsew", padx=40, pady=(30, 10))

        # configurar columnas del panel superior
        panel_superior.grid_columnconfigure((0, 1, 2), weight=1, uniform="col")

        # titulo
        ctk.CTkLabel(panel_superior,
                     text="Porcentajes de Macros",
                     font=("Segoe UI", 20, "bold"),
                     text_color="#6A0DAD").grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # columna 1 - Proteína
        ctk.CTkLabel(panel_superior, text="Proteína").grid(row=1, column=0, pady=(0, 5))
        self.entry_porcentaje_prote = ctk.CTkEntry(panel_superior, width=100)
        self.entry_porcentaje_prote.grid(row=2, column=0, pady=(0, 10))

        # columna 2 - Grasa
        ctk.CTkLabel(panel_superior, text="Grasa").grid(row=1, column=1, pady=(0, 5))
        self.entry_porcentaje_grasa = ctk.CTkEntry(panel_superior, width=100)
        self.entry_porcentaje_grasa.grid(row=2, column=1, pady=(0, 10))

        # columna 3 - Carbohidratos
        ctk.CTkLabel(panel_superior, text="Carbohidratos").grid(row=1, column=2, pady=(0, 5))
        self.entry_porcentaje_carb = ctk.CTkEntry(panel_superior, width=100)
        self.entry_porcentaje_carb.grid(row=2, column=2, pady=(0, 10))

        # boton de calcular
        btn_calcular = ctk.CTkButton(panel_superior,
                                     text="Generar Tabla",
                                     font=("Segoe UI", 14),
                                     width=150,
                                     height=45,
                                     corner_radius=14,
                                     fg_color="#6A0DAD",
                                     hover_color="#5a089e",
                                     text_color="white",
                                     command=self.calcular_macros)
        btn_calcular.grid(row=3, column=1, pady=(20, 10))

        # ===== Panel inferior =====
        panel_inferior = ctk.CTkFrame(self, fg_color="transparent")
        panel_inferior.grid(row=1, column=0, padx=40, pady=(10, 20), sticky="nsew")
        panel_inferior.grid_columnconfigure((0, 1, 2), weight=1)

        # titulo
        ctk.CTkLabel(panel_inferior,
                    text="🧾 Tabla Resultados",
                    font=("Segoe UI", 20, "bold"),
                    text_color="#6A0DAD").grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # label de error
        self.label_error = ctk.CTkLabel(panel_inferior, text="", text_color="red")
        self.label_error.grid(row=3, column=0, columnspan=3, pady=(5, 10))
        self.label_error.grid_remove()

        # tabla vacia inicial 
        self.panel_inferior = panel_inferior
        self.generar_tabla_resultados()


        # volver atras 
        self.btn_volver = ctk.CTkButton(panel_inferior,
                                        text="← Volver",
                                        width=100,
                                        fg_color="#6A0DAD",
                                        text_color="white",
                                        corner_radius=14,
                                        command = self.accion_btn_atras)
        self.btn_volver.grid(row=4, column=1, pady=(0, 10))

        # Botón nuevo paciente
        self.btn_nuevo_paciente = ctk.CTkButton(panel_inferior,
                                                text="➕ Nuevo Paciente",
                                                width=150,
                                                fg_color="#6A0DAD",
                                                text_color="white",
                                                corner_radius=14,
                                                command=self.nuevo_paciente)
        self.btn_nuevo_paciente.grid(row=5, column=1, pady=(0, 10))




    # obtener el GET desde otro frame
    def set_resultado(self, get_obtenido, peso_paciente):
        self.get = get_obtenido
        self.peso = peso_paciente

        self.label_get = ctk.CTkLabel(self.panel_inferior,
                              text=f"GET total: {self.get} kcal/día",
                              font=("Segoe UI", 14, "bold"),
                              text_color="#6A0DAD")
        self.label_get.grid(row=2, column=0, columnspan=3, pady=(0, 10))


    # calcular distribucion de macros
    def calcular_macros(self):
        porcentajes_macros = {}

        try:
            porcentaje_prote = validar_entero(self.entry_porcentaje_prote, "Porcentaje Proteína")
            porcentaje_grasa = validar_entero(self.entry_porcentaje_grasa, "Porcentaje Grasas")
            porcentaje_carb = validar_entero(self.entry_porcentaje_carb, "Porcentaje CHO")

            if porcentaje_carb + porcentaje_prote + porcentaje_grasa > 100:
                raise ValueError("La suma de todos los macros no puede ser mayor a 100")

            elif porcentaje_carb + porcentaje_prote + porcentaje_grasa != 100:
                raise ValueError("La suma de los porcentajes debe ser 100")
            self.label_error.grid_remove()


        except ValueError as e:
            self.label_error.configure(text=str(e))
            self.label_error.grid()
        
        else:

            porcentajes_macros["proteina"] = porcentaje_prote
            porcentajes_macros["hidratos_carbono"] = porcentaje_carb
            porcentajes_macros["grasa"] = porcentaje_grasa


            kcal_macros = calcular_kcal_macro(porcentajes_macros, self.get)
            g_macros = calcular_g_macros(kcal_macros)
            g_macros_peso = calcular_g_peso(self.peso, g_macros) 

            datos_tabla = [
                [  
                    round(g_macros["hidratos_carbono"], 2),
                    round(g_macros["grasa"], 2),
                    round(g_macros["proteina"], 2)
                ],
                [  
                    round(g_macros_peso["hidratos_carbono"], 2),
                    round(g_macros_peso["grasa"], 2),
                    round(g_macros_peso["proteina"], 2)
                ]
            ]

            self.generar_tabla_resultados(datos_tabla)


        
       
    # generar tabla
    def generar_tabla_resultados(self, datos=None):
        # Eliminar tabla previa si existe
        if hasattr(self, "tabla_frame"):
            self.tabla_frame.destroy()

        # Cabeceras y filas
        headers = ["CHO", "Grasa", "Proteína"]
        rows_nombres = ["g / día", "g / kg / día"]
        tabla_colores = {
            "cabecera": "#37474F",   # gris azulado oscuro
            "texto_cabecera": "white",
            "fila_par": "#F5F5F5",   # gris claro
            "fila_impar": "#EEEEEE", # gris aún más claro
            "texto": "#000000"
        }

        # Frame principal de tabla
        self.tabla_frame = ctk.CTkFrame(self.panel_inferior, fg_color="white", corner_radius=10)
        self.tabla_frame.grid(row=1, column=0, columnspan=3, pady=(5, 10))


        # ---- Fila de Cabecera ----
        fila_header = ctk.CTkFrame(self.tabla_frame, fg_color=tabla_colores["cabecera"])
        fila_header.pack(fill="x", pady=1)

        # Celda vacía (esquina)
        ctk.CTkLabel(fila_header, text="", width=80, text_color=tabla_colores["texto_cabecera"],
                    fg_color=tabla_colores["cabecera"]).pack(side="left")

        # Cabeceras
        for encabezado in headers:
            ctk.CTkLabel(fila_header, text=encabezado, font=("Segoe UI", 12, "bold"),
                        text_color=tabla_colores["texto_cabecera"], width=100,
                        fg_color=tabla_colores["cabecera"]).pack(side="left", padx=1)

        # ---- Filas de datos ----
        for i, nombre_fila in enumerate(rows_nombres):
            bg = tabla_colores["fila_par"] if i % 2 == 0 else tabla_colores["fila_impar"]

            fila = ctk.CTkFrame(self.tabla_frame, fg_color=bg)
            fila.pack(fill="x")

            # Etiqueta lateral (fila)
            ctk.CTkLabel(fila, text=nombre_fila, width=80,
                        text_color=tabla_colores["texto"]).pack(side="left", padx=1)

            # Valores de la fila
            for j in range(len(headers)):
                valor = datos[i][j] if datos else ""
                ctk.CTkLabel(fila, text=str(valor), font=("Segoe UI", 12),
                            text_color=tabla_colores["texto"], width=100).pack(side="left", padx=1)


    # funcion del boton
    def accion_btn_atras(self):
        
        if hasattr(self, "tabla_frame"):
            self.tabla_frame.destroy()
            self.generar_tabla_resultados()


        if hasattr(self, "label_get"):
            self.label_get.grid_remove()

        if hasattr(self, "label_error"):
            self.label_error.configure(text="")
            self.label_error.grid_remove()

        self.entry_porcentaje_prote.delete(0, "end")
        self.entry_porcentaje_grasa.delete(0, "end")
        self.entry_porcentaje_carb.delete(0, "end")

        self.label_get.destroy()

        self.get = None
        self.peso = None

        self.cambiar_frame_callback("get_inicio")

    # funcion boton nuevo paciente
    def nuevo_paciente(self):

        frame_inicio = self.master.frames["get_inicio"]
        
        frame_inicio.volver_inicio()

        self.accion_btn_atras()