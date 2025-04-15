import customtkinter as ctk

class GetTablaFrame(ctk.CTkFrame):
    def __init__(self, master, cambiar_frame_callback):
        super().__init__(master)

        # Título
        ctk.CTkLabel(self, text="Resultados del cálculo GET", font=("Arial", 18)).pack(pady=20)

        # Resultado simulado (luego puedes reemplazar con datos reales)
        self.resultado_label = ctk.CTkLabel(self, text="Aquí se mostrarán los resultados...", font=("Arial", 14))
        self.resultado_label.pack(pady=10)

        # Botón para volver
        ctk.CTkButton(self, text="Volver al formulario", command=lambda: cambiar_frame_callback("get_inicio")).pack(pady=10)
        ctk.CTkButton(self, text="Volver al inicio", command=lambda: cambiar_frame_callback("inicio")).pack(pady=10)

    # Esta función la puedes usar para pasarle datos desde el formulario
    def mostrar_resultado(self, texto):
        self.resultado_label.configure(text=texto)
