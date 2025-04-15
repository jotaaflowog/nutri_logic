import customtkinter as ctk

class ExcelFrame(ctk.CTkFrame):
    def __init__(self, master, cambiar_frame_callback):
        super().__init__(master)

        # Título
        ctk.CTkLabel(self, text="Calculadora G (por Excel)", font=("Arial", 18)).pack(pady=20)

        # Mensaje placeholder
        ctk.CTkLabel(self, text="🛠️ Esta función estará disponible próximamente.", font=("Arial", 14)).pack(pady=10)

        # Botón para volver
        ctk.CTkButton(self, text="Volver al inicio", command=lambda: cambiar_frame_callback("inicio")).pack(pady=20)
