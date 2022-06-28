import pandas as pd
import plotly
import plotly.express as px
from peakdetect import peakdetect
import numpy as np
import matplotlib.pyplot as plt 

# Einlesen einer csv-Datei aus landmark_results_combined_new
df = pd.read_csv(
    "landmark_results_combined_new/4_Joggen_combined.csv"
)

# Liniendiagramm mit y-Achse Distanz rechte Hüfte - Knie und dessen Anomalieerkennungswerte(0 oder 1)
# Um Z-Score hinzuzufügen: 1. In Datei evaluate_distances.py Zeile 63 (drop columns) auskommentieren, in Zeile 69 df_anomalien zu df ändern und Dateien generieren, Zielordner davor leeren.
# 2. In Liste für y-Achse (diese Datei, Zeile 11) noch "z_rightkneehip" hinzufügen

fig1= px.line(df, x=df.index, y=['LEFT_FOOT_INDEX_x_back','LEFT_HEEL_x_back', 'LEFT_HEEL_y_site'], title='X-Werte Fußspitze und Ferse hinten')
fig1.show()

# Anzeigen der Tiefpunkte
relevant_column = df["LEFT_FOOT_INDEX_y_site"]
peaks = peakdetect(relevant_column, lookahead=13)
lowerPeaks = np.array(peaks[1])

plt.plot(relevant_column)
plt.plot(lowerPeaks[:,0], lowerPeaks[:,1], 'ko')
plt.show()