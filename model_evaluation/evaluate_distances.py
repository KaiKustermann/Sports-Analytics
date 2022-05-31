import numpy as np
import pandas as pd
import scipy.stats as stats
import glob

# Alle Datei-Namen (.csv) aus Ordner distances in eine Liste laden
files = []
for file in glob.glob("model_evaluation/distances/*.csv"):
    files.append(file)

# Funktion, um Z-Werte einzuordnen. Rückgabewert 0 für keine Anomalie, 1 für Anomalie
def check_anomalien(z):
    if z < 3:
        return 0

    else:
        return 1

# Schleife: Erstellen einer neuen CSV-Datei mit evaluierten Distanzen: Enthält Distanzen und Anomalieprüfung
for i in files:

    # Einlesen der Datei in Dataframe
    df = pd.read_csv(i)

    # Berechnungen Z-Werte pro Feature/Distanz und speichern in neues Column
    df["z_hips"] = np.abs(stats.zscore(df["distance_hips"]))

    df["z_leftkneehip"] = np.abs(stats.zscore(df["distance_leftkneehip"]))
    df["z_rightkneehip"] = np.abs(stats.zscore(df["distance_rightkneehip"]))

    df["z_leftkneeankle"] = np.abs(stats.zscore(df["distance_leftkneeankle"]))
    df["z_rightkneeankle"] = np.abs(stats.zscore(df["distance_rightkneeankle"]))

    df["z_leftkneeheel"] = np.abs(stats.zscore(df["distance_leftkneeheel"]))
    df["z_rightkneeheel"] = np.abs(stats.zscore(df["distance_rightkneeheel"]))

    df["z_leftankleindex"] = np.abs(stats.zscore(df["distance_leftankleindex"]))
    df["z_rightankleindex"] = np.abs(stats.zscore(df["distance_rightankleindex"]))

    df["z_leftheelindex"] = np.abs(stats.zscore(df["distance_leftheelindex"]))
    df["z_rightheelindex"] = np.abs(stats.zscore(df["distance_rightheelindex"]))


    # Anwenden der Funktion check_anomalien auf jedes Column der Z-Werte und speichern der Rückgabewerte in neues Column
    df['distance_hips_anomalien'] = df['z_hips'].apply(check_anomalien)

    df['distance_leftkneehips_anomalien'] = df['z_leftkneehip'].apply(check_anomalien)
    df['distance_rightkneehips_anomalien'] = df['z_rightkneehip'].apply(check_anomalien)

    df['distance_leftkneeankle_anomalien'] = df['z_leftkneeankle'].apply(check_anomalien)
    df['distance_rightkneeankle_anomalien'] = df['z_rightkneeankle'].apply(check_anomalien)

    df['distance_leftkneeheel_anomalien'] = df['z_leftkneeheel'].apply(check_anomalien)
    df['distance_rightkneeheel_anomalien'] = df['z_rightkneeheel'].apply(check_anomalien)

    df['distance_leftankleindex_anomalien'] = df['z_leftankleindex'].apply(check_anomalien)
    df['distance_rightankleindex_anomalien'] = df['z_rightankleindex'].apply(check_anomalien)

    df['distance_leftheelindex_anomalien'] = df['z_leftheelindex'].apply(check_anomalien)
    df['distance_rightheelindex_anomalien'] = df['z_rightheelindex'].apply(check_anomalien)

    # Entfernen aller Columns mit Z-Werten, optional
    df_anomalien = df.drop(["z_hips", "z_leftkneehip","z_rightkneehip", "z_leftkneeankle","z_rightkneeankle", "z_leftkneeheel","z_rightkneeheel", "z_leftankleindex", "z_rightankleindex", "z_leftheelindex", "z_rightheelindex"], axis=1)

    # Pfad der csv-Datei aufsplitten, benötigt für Speichern neuer Datei
    x = i.split("/")

    # Je csv-Datei erstellen einer neuen csv-Datei mit Evaluationswerten in Ordner evaluated_distances
    df_anomalien.to_csv("model_evaluation/evaluated_distances/" + "evaluated_" + x[2], index=False)