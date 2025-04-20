import os
import sys
import customtkinter as ctk
from frontend.frames.frames_inicio import InicioFrame
from frontend.frames.frames_get_inicio import GetInicioFrame
from frontend.frames.frames_get_tabla import GetTablaFrame
from frontend.frames.frames_excel import ExcelFrame

def obtener_ruta_recurso(ruta_relativa):
    """Obtiene la ruta absoluta al recurso, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, ruta_relativa)


class NutriLogicApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NutriLogic")
        self.geometry("800x600")
        ruta_icono = obtener_ruta_recurso('assets/logo.ico')
        self.iconbitmap(ruta_icono)
        self.resizable(False, False)

        # Frames
        self.frames = {
            "inicio": InicioFrame(self, self.cambiar_frame),
            "get_inicio": GetInicioFrame(self, self.cambiar_frame),
            "get_tabla": GetTablaFrame(self, self.cambiar_frame),
            "excel": ExcelFrame(self, self.cambiar_frame),
        }

        self.cambiar_frame("inicio")

    def cambiar_frame(self, nombre):
        for frame in self.frames.values():
            frame.pack_forget()

        self.frames[nombre].pack(fill="both", expand=True)
