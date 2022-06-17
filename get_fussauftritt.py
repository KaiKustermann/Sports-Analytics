from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob

#Einlesen einer csv-Datei
#df = pd.read_csv("landmark_results_combined_new/4_Gehen_combined.csv")
#df = df.iloc[:, 1:]

# Funktion um Fußauftritt einzuordnen
def check_auftritt(x, y):
        
    if x < y:
        return "Vorfußlauf"
    if x > y:
        return "Fersenlauf"
    else:
        return "Mittelfußlauf"

files = []
for file in glob.glob("landmark_results_combined_new/*.csv"):
    files.append(file)

for x in files:

    df = pd.read_csv(x)
    df = df.iloc[:, 1:]

    relevant_column = df["LEFT_HEEL_y_site"]

    #Analysieren der Peaks (High und Low)
    peaks = peakdetect(relevant_column, lookahead=15)
    # Lookahead is the distance to look ahead from a peak to determine if it is the actual peak. 
    # Change lookahead as necessary 
    #higherPeaks = np.array(peaks[0])

    # Lower Peaks (Tiefpunkte) und deren Index abspeichern
    lowerPeaks = np.array(peaks[1])
    index_lowerPeaks = lowerPeaks[:,0]

    ### ZIEL: csv-Datei mit Zyklustiefpunkt LEFT_FOOT_INDEX_y_site und LEFT_HEEL_y_site
    # Leeren DataFrame mit Spalten für alten Index, Fußspitze und Ferse erstellen
    dfObj = pd.DataFrame(columns=['old_index', 'LEFT_FOOT_INDEX_y_site', 'LEFT_HEEL_y_site'])

    # Durch Indizes iterieren und für jeden Index in Liste den Wert Fußspitze und Ferse in den neuen DF speichern
    for i in index_lowerPeaks:
        #new_df = df["LEFT_FOOT_INDEX_y_site"][i]
        #dfObj = dfObj.append({'old_index': i,'LEFT_FOOT_INDEX_y_site': df["LEFT_FOOT_INDEX_y_site"][i], 'LEFT_HEEL_y_site': df['LEFT_HEEL_y_site'][i]}, ignore_index=True)
        dfObj = pd.concat([dfObj, pd.DataFrame.from_records([{'old_index': i,'LEFT_FOOT_INDEX_y_site': df["LEFT_FOOT_INDEX_y_site"][i], 'LEFT_HEEL_y_site': df['LEFT_HEEL_y_site'][i]}])], ignore_index=True)
    # Funktion auf jede Reihe anwenden
    dfObj["Klasse"] = dfObj.apply(lambda row: check_auftritt(row['LEFT_FOOT_INDEX_y_site'], row['LEFT_HEEL_y_site']), axis=1)

    print("Für File", x, dfObj['Klasse'].value_counts())