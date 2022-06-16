import pandas as pd
import plotly
import plotly.express as px

# Einlesen einer csv-Datei aus evaluated_distances
df = pd.read_csv(
    "landmark_results_combined_new/1_Joggen_combined.csv"
)

# Liniendiagramm mit y-Achse Distanz rechte Hüfte - Knie und dessen Anomalieerkennungswerte(0 oder 1)
# Um Z-Score hinzuzufügen: 1. In Datei evaluate_distances.py Zeile 63 (drop columns) auskommentieren, in Zeile 69 df_anomalien zu df ändern und Dateien generieren, Zielordner davor leeren.
# 2. In Liste für y-Achse (diese Datei, Zeile 11) noch "z_rightkneehip" hinzufügen
fig1 = px.line(
    df,
    x=df.index,
    y="LEFT_FOOT_INDEX_y_site",
    title="Test",
)
fig1.show()

