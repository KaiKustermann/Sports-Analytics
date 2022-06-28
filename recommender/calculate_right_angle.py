import math
from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob
import statistics
from calculate_fussstellung_adjusted import calculate_fussstellung_adjusted

def calculate_right_angle():
    # csv-Dateien der Videos, die von Expertin als "Neutrale Fußstellung" kategorisiert wurden
    files = ["landmark_results_combined_new/8_Gehen_combined.csv", "landmark_results_combined_new/4_Gehen_combined.csv",
    "landmark_results_combined_new/2_Gehen_combined.csv", "landmark_results_combined_new/10_Gehen_combined.csv"]

    # Variablen zum Zählen und Berechnen des Mittelwerts
    mw = 0
    count = 0

    # Für alle files aus der Liste
    for x in files:

        # Einlesen der Dateien
        dffile = pd.read_csv(x)
        lookahead= 15
        dffile=dffile.iloc[:, 1:]

        # Erkennen der Hoch-/Tiefpunkte
        relevant_column = dffile["LEFT_HEEL_y_site"]
        peaks = peakdetect(relevant_column, lookahead=lookahead)

        # Tiefpunkte erkennen
        lowerPeaks = np.array(peaks[1])
        df2 = pd.DataFrame(lowerPeaks, columns = ['old_index','value'])
        indices = lowerPeaks[:,0]
        values = lowerPeaks[:,1]

        # Sortieren der Tiefpunkte, Median bestimmen
        sorted_df = df2.sort_values(by=['value'], ignore_index=True)
        median = statistics.median_low(sorted_df["value"])
        index_median = sorted_df.index[sorted_df['value'] == median].tolist()
        # 10 Werte rund um Median abspeichern
        neue_liste = sorted_df.iloc[index_median[0] - 10 : index_median[0] + 10]
        # Alter Index zu Liste
        liste = neue_liste['old_index'].tolist()

        # Indizes durchgehen
        for i in liste:

            # Winkelberechnung zwischen Knöchel gerade herunter und Knöchel-Ferse
            b = np.array([dffile.LEFT_ANKLE_x_back[i], dffile.LEFT_ANKLE_y_back[i]])
            a = np.array([dffile.LEFT_ANKLE_x_back[i], dffile.LEFT_HEEL_y_back[i]])
            c = np.array([dffile.LEFT_HEEL_x_back[i], dffile.LEFT_HEEL_y_back[i]])

            ba = a - b
            bc = c - b

            cosine_angle1 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
            angle1 = np.arccos(cosine_angle1)

            # Jeden Winkel Zählen und Addieren
            count = count + 1
            mw = mw + np.degrees(angle1)

    # Mittelwert berechnen und diesen von 180 Grad abziehen
    medium_angle = (mw / count)
    right_angle = 180 - medium_angle

    # Berechnen der Fußstellung für alle Dateien mit neuem Winkel
    calculate_fussstellung_adjusted(right_angle)