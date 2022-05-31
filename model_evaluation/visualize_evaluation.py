import pandas as pd
import plotly
import plotly.express as px

# Einlesen einer csv-Datei aus evaluated_distances
df = pd.read_csv(
    "model_evaluation/evaluated_distances/evaluated_distances_7_Joggen_combined.csv"
)

# Liniendiagramm mit y-Achse Distanz rechte Hüfte - Knie und dessen Anomalieerkennungswerte(0 oder 1)
# Um Z-Score hinzuzufügen: 1. In Datei evaluate_distances.py Zeile 63 (drop columns) auskommentieren, in Zeile 69 df_anomalien zu df ändern und Dateien generieren, Zielordner davor leeren.
# 2. In Liste für y-Achse (diese Datei, Zeile 11) noch "z_rightkneehip" hinzufügen
fig1 = px.line(
    df,
    x=df.index,
    y=["distance_rightkneehip", "distance_rightkneehips_anomalien"],
    title="Anomalien Hüfte - Knie rechts",
)
fig1.show()

# Um die Ergebnisse der Evaluation der einzelnen Koordinaten zu visualisieren:
# csv-Datei und zu zeigende Features können angepasst werden
df = pd.read_csv("model_evaluation/evaluated_keypoints/evaluated_7_Joggen_combined.csv")

fig2 = px.line(
    df, x=df.index, y=["LEFT_HIP_x_back", "a_lefthipx"], title="Anomalien LEFT_HIP_X"
)
fig2.show()
