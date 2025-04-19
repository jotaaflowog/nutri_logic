import customtkinter as ctk

class ExcelFrame(ctk.CTkFrame):
    def __init__(self, master, cambiar_frame_callback):
        super().__init__(master) 
        self.configure(fg_color="#F9F9FB")

        # Panel centrado
        self.panel = ctk.CTkFrame(self, fg_color="transparent")
        self.panel.place(relx=0.5, rely=0.5, anchor="center") 

        # Título
        ctk.CTkLabel(
            self.panel,
            text="Calculadora de Alimentos",
            font=("Segoe UI", 18, "bold"),
            text_color="#6A0DAD"
        ).pack(pady=(0, 10))

        # Mensaje informativo
        ctk.CTkLabel(
            self.panel,
            text="🔧 Esta función estará disponible próximamente.",
            font=("Segoe UI", 14),
            text_color="#555555"
        ).pack(pady=(0, 20))

        # Botón para volver al inicio
        ctk.CTkButton(
            self.panel,
            text="← Volver al inicio",
            width=180,
            fg_color="#6A0DAD",
            text_color="white",
            corner_radius=14,
            command=lambda: cambiar_frame_callback("inicio")
        ).pack()
