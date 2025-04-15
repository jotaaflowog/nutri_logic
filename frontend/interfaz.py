import customtkinter as ctk
from frontend.frames.frames_inicio import InicioFrame
from frontend.frames.frames_get_inicio import GetInicioFrame
from frontend.frames.frames_get_tabla import GetTablaFrame
from frontend.frames.frames_excel import ExcelFrame


class NutriLogicApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NutriLogic")
        self.geometry("800x600")
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
