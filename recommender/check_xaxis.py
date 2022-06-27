import math
from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob
import statistics

# Prüfen, ob der linke oder der rechte Punkt der hinteren Ansicht die Ferse ist
# Dadurch kann der Grundwinkel (180 oder geringer) angepasst werden
df = pd.read_csv(
    "landmark_results_combined_new/2_Joggen_combined.csv"
)
lookahead = 13
df=df.iloc[:, 1:]
relevant_column = df["LEFT_HEEL_y_site"]
peaks = peakdetect(relevant_column, lookahead=lookahead)
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

# Überprüfen, welcher Punkt der Linke ist
def check_location(footindex, ferse):
    if footindex < ferse:
        print("Fußspitze ist der linke Punkt")
    else:
        print("Ferse ist der linke Punkt")


for i in index_lowerPeaks:
    # Für jeden Tiefpunkt, überprüfe Location
    footindex = df["LEFT_FOOT_INDEX_x_back"][i]
    ferse = df["LEFT_HEEL_x_back"][i]
    check_location(footindex, ferse)
