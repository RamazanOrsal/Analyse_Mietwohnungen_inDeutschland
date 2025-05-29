# 🏠 Analyse der Mietwohnungen in Deutschland

Dieses Projekt ist eine datengestützte Analyse von Mietwohnungen in Deutschland auf Basis eines umfangreichen Datensatzes von **ImmoScout24**, der über [Kaggle](https://www.kaggle.com/) bezogen wurde. Ziel ist es, regionale Unterschiede, Preisstrukturen, Ausstattungseinflüsse und Wohntrends auf dem deutschen Mietwohnungsmarkt sichtbar zu machen.

## 📊 Verwendete Daten

- **Quelle**: ImmoScout24 via Kaggle  
- **Datenart**: Mietwohnungsangebote (keine Kaufangebote)  
- **Zeitraum der Erhebung**: 22.09.2018, 10.05.2019 und 08.10.2019  
- **Umfang**: Ca. 250.000 Einträge aus allen Bundesländern  

> **Hinweis**: Aufgrund der Dateigröße wird der Datensatz **nicht direkt im Repository gespeichert**. Du findest ihn auf Kaggle unter folgendem Link:  
> [Zum Datensatz auf Kaggle](https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany)

  
# 🛠️ Verwendete Technologien

-**Programmiersprache**: Python
- **Datenbank**: CSV-Dateien (lokale Datenverarbeitung ohne Datenbanksystem)
-**Bibliotheken**:  Pandas, Numpy, Matplotlib, Seaborn  
- Entwickelt mit Visual Studio Code


## 🎯 Projektziele

- Analyse der Mietwohnungsverteilung nach Bundesland  
- Vergleich der durchschnittlichen Mietpreise  
- Untersuchung des Einflusses von Ausstattungsmerkmalen (z. B. Balkon, Aufzug)  
- Visualisierung der Preisverteilung (Histogramm & Boxplot)  
- Analyse des Zusammenhangs zwischen Wohnfläche und Gesamtmiete  
- Auswertung der Heizsysteme in deutschen Mietwohnungen


## 🧭 Struktur der Analyse (Menüpunkte)

1-Zeige die Gesamtzahl der Mietwohnungen nach Bundesland
2-Zeige die durchschnittliche Miete nach Bundesland.
3-Zeige die durchschnittliche Miete nach Merkmalen
4-Zeige die Zahl der Mietwohnungen
5-Zeige die Miete nach Wohnfläche und Zeige Durchschnittlicher m²-Preis nach Bundesland
6-Zeige die Verteilung der Wohnungen nach Heizungsart
7-Beenden


## 🗂️ Enthaltene Dateien

- `Immoscout.pptx` – Präsentation mit Grafiken und Ergebnissen  
- `Histogramm-Diagramm.pdf` – Alle Histogramme, Boxplots nach Bundesländer im PDF-Format 
- `Scatterplot-Diagramm.pdf` – Alle Scatterplot nach Bundesländer im PDF-Format 
- `startseite.py` – Hauptmenü zur Steuerung der Analysefunktionen.
- `data_proje.py` – Visualisierungs- und Analysecode
- **Datensatz** – extern auf Kaggle verfügbar



