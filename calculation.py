# Berechnungsfunktion
def calculate(expression):
    try:
        # eval für die Berechnung des Ausdrucks
        return eval(expression)
    except Exception:
        return "Error"
