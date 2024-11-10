## Taschenrechner mit Python und CustomTkinter

Ein einfacher GUI-basierter Taschenrechner, entwickelt in Python mit der customtkinter-Bibliothek. Dieses Projekt unterstützt grundlegende mathematische Berechnungen und bietet eine anpassbare Benutzeroberfläche mit Themes, die in einer JSON-Datei definiert sind.

### Inhaltsverzeichnis
- Überblick
- Features
- Voraussetzungen
- Installation
- Projektstruktur
- Verwendung
- Theme-Anpassung
- Lizenz

### Überblick
Dieser Taschenrechner ermöglicht die Durchführung von Grundrechenarten wie Addition, Subtraktion, Multiplikation und Division. Die Oberfläche ist mit customtkinter erstellt und verwendet eine JSON-Datei (lightblue.json), die Farben und UI-Styles definiert. So kann das Aussehen des Rechners einfach angepasst werden.

### Features
- Unterstützt Addition, Subtraktion, Multiplikation und Division.
- Benutzerdefinierte Themes durch eine JSON-Datei.
- Einfache und intuitive Benutzeroberfläche.

### Voraussetzungen
- Python 3.7 oder höher: [Download Python](https://www.python.org/downloads/)
- customtkinter-Bibliothek: Installierbar über pip.

### Installation
Python und Abhängigkeiten installieren:

1. Installiere customtkinter:
    ```sh
    pip install customtkinter
    ```

2. Projekt klonen:
    ```sh
    git clone https://github.com/Patzyh/calculater
    cd calculator_project
    ```

3. Projektstruktur überprüfen:
    Stelle sicher, dass alle Dateien im richtigen Verzeichnis liegen, besonders die Datei `lightblue.json` im Ordner `resources`.

### Projektstruktur
```plaintext
calculator_project/
│
├── [`main.py`](main.py )              # Startskript der Anwendung
├── [`ui.py`](ui.py )                # UI-Komponenten und Logik der Benutzeroberfläche
├── [`calculation.py`](calculation.py )       # Berechnungslogik für den Taschenrechner
│
└── resources/
    ├── [`recources/lightblue.json`](recources/lightblue.json )   # JSON-Datei zur Anpassung des Farbschemas
    └── Aovel.ttf        # Benutzerdefinierte Schriftart für die Oberfläche
```

### Verwendung
Der Taschenrechner bietet die folgenden Tasten und Funktionen:

- **Zifferntasten (0-9)**: Fügt die entsprechende Ziffer zum aktuellen Ausdruck hinzu.
- **Punkt (.)**: Fügt einen Dezimalpunkt zum aktuellen Ausdruck hinzu.
- **Operatoren (+, -, *, /)**: Fügt den entsprechenden mathematischen Operator zum aktuellen Ausdruck hinzu.
- **Gleichheitszeichen (=)**: Berechnet das Ergebnis des aktuellen Ausdrucks und zeigt es an.
- **C**: Löscht den aktuellen Ausdruck und setzt das Ergebnis auf "0".

### Theme-Anpassung
Die Farben und Stile des Taschenrechners können durch Bearbeiten der `lightblue.json`-Datei im Ordner `resources` angepasst werden. Diese Datei enthält die Farbschemata und UI-Styles für verschiedene Komponenten der Benutzeroberfläche.

### Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE) Datei.
