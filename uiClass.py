import customtkinter
from tkextrafont import Font

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x600")

        customtkinter.set_appearance_mode("dark")

        try:
            Font(file="resources/Aovel.ttf")
        except Exception as e:
            print(f"Error loading font: {e}")

        self.create_widgets()

    def clear_site(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_widgets(self):
        self.entry = customtkinter.CTkEntry(self, font=("Aovel", 20))
        self.entry.pack(fill="x")

        self.__buttons = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["C", "0", "=", "/"]
        ]

        for row in self.__buttons:
            self.clear_site()

            self.__button = []

            for i in range(10):
                self.__button.append(
                    customtkinter.CTkButton(self, text=str(i), command=lambda i=i: self.button_click(i), height=50, width=50, font=("Inter Black", 14), fg_color="#84817a"))
                self.__button[i - 1].place(x=10 + ((i - 1) % 3) * 55, y=105 + ((i - 1) // 3) * 55)