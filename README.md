## Taschenrechner mit Python und CustomTkinter

Ein einfacher GUI-basierter Taschenrechner, entwickelt in Python mit der customtkinter-Bibliothek. Dieses Projekt unterstützt grundlegende mathematische Berechnungen und bietet eine anpassbare Benutzeroberfläche mit Themes, die in einer JSON-Datei definiert sind.

### Inhaltsverzeichnis
- Überblick
- Screenshot
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
├── [main.py](http://_vscodecontentref_/0)              # Startskript der Anwendung
├── [ui.py](http://_vscodecontentref_/1)                # UI-Komponenten und Logik der Benutzeroberfläche
├── [calculation.py](http://_vscodecontentref_/2)       # Berechnungslogik für den Taschenrechner
│
└── resources/
    ├── [lightblue.json](http://_vscodecontentref_/3)   # JSON-Datei zur Anpassung des Farbschemas
    └── Aovel.ttf        # Benutzerdefinierte Schriftart für die Oberfläche