from frontend.interfaz import NutriLogicApp
import customtkinter as ctk


if __name__ == '__main__':
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")  
    app = NutriLogicApp()
    app.mainloop()


