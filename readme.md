# LB 324
## Azure Link:
https://gabrielkanalgalb324.azurewebsites.net/
## Aufgabe 2:
Erklären Sie hier, wie man `pre-commit` installiert.

Installation: Führen Sie pip install pre-commit im Terminal aus.

Konfigurationsdatei: Erstellen Sie eine .pre-commit-config.yaml im Projektverzeichnis.

Hooks hinzufügen: Fügen Sie die gewünschten Hooks wie flake8 oder black in die Konfigurationsdatei ein. Beispiel:

yaml
Copy code
repos:
  - repo: https://github.com/ambv/black
    rev: 23.7.0
    hooks:
      - id: black
        language_version: python3.11
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.0.0
    hooks:
      - id: check-yaml
      - id: check-added-large-files
Initialisierung: Führen Sie pre-commit install im Terminal aus.

Automatische Prüfung: Die festgelegten Prüfungen werden nun automatisch vor jedem Commit ausgeführt.

## Aufgabe 4:
Erklären Sie hier, wie Sie das Passwort aus Ihrer lokalen `.env` auf Azure übertragen.

In Azure unter Konfigurationen, muss man eine neue Anwendungseinstellung hinzufügen.
Name: PASSWORD
Wert: einSehrGeheimesPasswort

## Aufgabe 5:
Die Aufgabe 5 wurde zusammen mit der Aufgabe 3 gelöst.

