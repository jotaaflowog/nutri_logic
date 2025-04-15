import customtkinter as ctk
from datetime import datetime

class InicioFrame(ctk.CTkFrame):
    def __init__(self, master, cambiar_frame_callback):
        super().__init__(master)
        self.configure(fg_color="#F9F9FB")

        # Layout base
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        # Contenedor centrado
        contenedor = ctk.CTkFrame(self, fg_color="transparent")
        contenedor.grid(row=0, column=0)

        # Título
        ctk.CTkLabel(contenedor,
                     text="NutriLogic 🧠",
                     font=("Segoe UI", 36, "bold"),
                     text_color="#6A0DAD").pack(pady=(0, 6))

        # Subtítulo
        ctk.CTkLabel(contenedor,
                     text="Todo lo que necesitas en una sola aplicación.",
                     font=("Segoe UI", 16),
                     text_color="#444").pack(pady=(0, 40))

        # Botón GET
        ctk.CTkButton(contenedor,
                      text="🧮 Calcular GET",
                      font=("Segoe UI", 14),
                      width=250,
                      height=45,
                      corner_radius=14,
                      fg_color="#6A0DAD",
                      hover_color="#5a089e",
                      text_color="white",
                      command=lambda: cambiar_frame_callback("get_inicio")).pack(pady=10)

        # Botón Excel
        ctk.CTkButton(contenedor,
                      text="📊 Calculador de alimentos",
                      font=("Segoe UI", 14),
                      width=250,
                      height=45,
                      corner_radius=14,
                      fg_color="#6A0DAD",
                      hover_color="#5a089e",
                      text_color="white",
                      command=lambda: cambiar_frame_callback("excel")).pack(pady=10)

        # Footer
        hoy = datetime.today()
        ctk.CTkLabel(self,
                     text=f"Versión 1.0 • NutriLogic © {hoy.year} | JMBC"
,
                     font=("Segoe UI", 10),
                     text_color="#aaa").grid(row=1, column=0, pady=(10, 5))
