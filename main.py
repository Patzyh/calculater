import customtkinter as ctk
from ui import CalculatorUI

def main():
    ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = CalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
