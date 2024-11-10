import customtkinter as ctk
import json
from calculation import calculate

class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Taschenrechner")
        self.root.geometry("360x480")
        self.root.resizable(False, False)

        # Farben und Stile aus JSON-Datei laden
        with open("resources/lightblue.json", "r") as file:
            styles = json.load(file)

        # Farben und Stile festlegen
        button_color = styles["CTkButton"]["fg_color"][0]
        button_hover_color = styles["CTkButton"]["hover_color"][0]
        button_text_color = styles["CTkButton"]["text_color"][0]
        entry_bg_color = styles["CTkEntry"]["fg_color"][0]
        entry_border_color = styles["CTkEntry"]["border_color"][0]
        entry_text_color = styles["CTkEntry"]["text_color"][0]
        root_bg_color = styles["CTk"]["fg_color"][0]

        # Hintergrundfarbe des Fensters setzen
        self.root.configure(bg=root_bg_color)

        # Initialisiert den Ausdruck und das Ergebnis
        self.expression = ""
        self.result_var = ctk.StringVar()
        self.result_var.set("0")

        # Definiere den globalen Font
        self.font = ("resources/Aovel.ttf", 18)  # Aovel als Standard-Font

        # Eingabefeld für den Ausdruck und das Ergebnis
        self.display = ctk.CTkEntry(root, textvariable=self.result_var, font=("resources/Aovel.ttf", 20),
                                    justify="right", width=340, height=50,
                                    fg_color=entry_bg_color, border_color=entry_border_color, text_color=entry_text_color)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons erstellen
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        # Buttons zum Grid hinzufügen
        for button_text in buttons:
            button = ctk.CTkButton(root, text=button_text, width=70, height=60, font=self.font,
                                   fg_color=button_color, hover_color=button_hover_color,
                                   text_color=button_text_color,
                                   command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear-Button hinzufügen
        clear_button = ctk.CTkButton(root, text="C", width=280, height=60, font=self.font,
                                     fg_color=button_color, hover_color=button_hover_color,
                                     text_color=button_text_color, command=self.clear)
        clear_button.grid(row=row_val, column=0, columnspan=4, sticky="we", padx=5, pady=5)

    # Button-Klick-Ereignis
    def on_button_click(self, button_text):
        if button_text == "=":
            self.evaluate_expression()
        else:
            self.expression += str(button_text)
            self.result_var.set(self.expression)

    # Berechnungsfunktion aufrufen und Ergebnis anzeigen
    def evaluate_expression(self):
        result = calculate(self.expression)
        self.result_var.set(result)
        self.expression = str(result)

    # Anzeige zurücksetzen
    def clear(self):
        self.expression = ""
        self.result_var.set("0")
