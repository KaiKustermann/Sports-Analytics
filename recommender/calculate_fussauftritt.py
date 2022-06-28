from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob
import math
import statistics

# Funktion um Fußauftritt einzuordnen
def check_auftritt(fussspitze, ferse):
    # Differenz der Werte berechnen
    change = get_change(fussspitze, ferse)
    
    # Wenn Differenz kleiner -0.03 Vorderfußlauf
    if change < -0.03:
        return "Vorfußlauf"
    # Wenn Differenz größer 0.03 Fersenlauf
    if change > 0.03:
        return "Fersenlauf"
    # Wenn zwischen -0.03 und 0.03 Mittelfußlauf
    else:
        return "Mittelfußlauf"

# Funktion um Differenz zu berechnen
def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return current - previous
    except ZeroDivisionError:
        return float('inf')

def calculate_fussauftritt():
    # Alle csv-Dateien aus Ordner in Liste speichern
    files = []
    for file in glob.glob("landmark_results_combined_new/*.csv"):
        files.append(file)

    # Leerer Dataframe für Output
    dfresults = pd.DataFrame(columns=['filename', 'klasse_fußauftritt'])

    for x in files:

        # Einlesen der Datei
        df = pd.read_csv(x)
        df = df.iloc[:, 1:]

        relevant_column = df["LEFT_HEEL_y_site"]

        #Extrahieren der Geschwindigkeit aus Name der csv Datei
        video = x.split("/")
        video_splitted  = video[1]
        z = video_splitted.split("_")
        speed = z[1]

        #Lookahead je nach Geschwindigkeit anpassen
        if speed == "Joggen":
            lookahead = 13
        if speed == "Laufen":
            lookahead = 13
        if speed == "Gehen":
            lookahead = 15

        #Analysieren der Peaks (High und Low)
        peaks = peakdetect(relevant_column, lookahead=lookahead)
        # Lookahead is the distance to look ahead from a peak to determine if it is the actual peak. 
        # Change lookahead as necessary 
        #higherPeaks = np.array(peaks[0])

        # Lower Peaks (Tiefpunkte) und deren Index abspeichern
        lowerPeaks = np.array(peaks[1])
        # Dataframe Tiefpunkte mit Index erstellen
        df_lowerpeaks = pd.DataFrame(lowerPeaks, columns = ['old_index','value'])
        # Dataframe nach Tiefpunkten sortieren
        sorted_df = df_lowerpeaks.sort_values(by=['value'], ignore_index=True)
        # Median bestimmen
        median = statistics.median_low(sorted_df["value"])
        # Index des Medians bestimmen
        index_median = sorted_df.index[sorted_df['value'] == median].tolist()
        # Relevante Tiefpunkte (+/- 10 um Median) in Dataframe 
        relevant_peaks = sorted_df.iloc[index_median[0] - 10 : index_median[0] + 10]
        # Ursprüngliche Indizes in Liste zum iterieren
        index_lowerPeaks = relevant_peaks['old_index'].tolist()


        ### ZIEL: csv-Datei mit Zyklustiefpunkt LEFT_FOOT_INDEX_y_site und LEFT_HEEL_y_site
        # Leeren DataFrame mit Spalten für alten Index, Fußspitze und Ferse erstellen
        dfObj = pd.DataFrame(columns=['old_index', 'LEFT_FOOT_INDEX_y_site', 'LEFT_HEEL_y_site'])

        # Durch Indizes iterieren und für jeden Index in Liste den Wert Fußspitze und Ferse in den neuen DF speichern
        for i in index_lowerPeaks:
            dfObj = pd.concat([dfObj, pd.DataFrame.from_records([{'old_index': i,'LEFT_FOOT_INDEX_y_site': df["LEFT_FOOT_INDEX_y_site"][i], 'LEFT_HEEL_y_site': df['LEFT_HEEL_y_site'][i]}])], ignore_index=True)
        
        # Funktion auf jede Reihe anwenden
        dfObj["Klasse"] = dfObj.apply(lambda row: check_auftritt(row['LEFT_FOOT_INDEX_y_site'], row['LEFT_HEEL_y_site']), axis=1)
        
        # Zählen der verschiedenen Klassen
        valuecount = dfObj['Klasse'].value_counts()

        # Neues Dataframe befüllen: Dateiname plus häufigste Klasse
        dfresults = pd.concat([dfresults, pd.DataFrame.from_records([{'filename': z[0] + "_" + z[1],'klasse_fußauftritt': valuecount.idxmax()}])], ignore_index=True)

    print(dfresults)

    # Speichern des Ergebnis-Dataframe in csv-Datei in Ordner Ergebnisse
    dfresults.to_csv("recommender/ergebnisse/" + "results_fussauftritt.csv", index=False)
