import numpy as np
import pandas as pd
import scipy.stats as stats
import glob

# Alle Datei-Namen (.csv) in eine Liste laden
files = []
for file in glob.glob("model_evaluation/distances/*.csv"):
    files.append(file)

def check_anomalien(z):
    # print(z)
    if z < 3:
        return 0

    else:
        return 1

# Erstellen einer neuen CSV-Datei mit Distanzen für jede CSV-Datei mit Keypoints

for i in files:
    # Einlesen der Datei in Dataframe
    df = pd.read_csv(i)

    # Finden des absoluten Werts des Z-Werts für jede Beobachtung
    z = np.abs(stats.zscore(df))
    # print(z)
    df["Z-Wert Hips"] = z.iloc[:, :1]

    df["Z-Wert LKHi"] = z.iloc[:, 1:2]
    df["Z-Wert RKHi"] = z.iloc[:, 2:3]

    df["Z-Wert LKHe"] = z.iloc[:, 3:4]
    df["Z-Wert RKHe"] = z.iloc[:, 4:5]

    df["Z-Wert LHI"] = z.iloc[:, 5:6]
    df["Z-Wert RHI"] = z.iloc[:, 6:7]

    df['distance_hips_anomalien'] = df['Z-Wert Hips'].apply(check_anomalien)

    df['distance_leftkneehips_anomalien'] = df['Z-Wert LKHi'].apply(check_anomalien)
    df['distance_rightkneehips_anomalien'] = df['Z-Wert RKHi'].apply(check_anomalien)

    df['distance_leftkneeheel_anomalien'] = df['Z-Wert LKHe'].apply(check_anomalien)
    df['distance_rightkneeheel_anomalien'] = df['Z-Wert RKHe'].apply(check_anomalien)

    df['distance_leftheelindex_anomalien'] = df['Z-Wert LHI'].apply(check_anomalien)

    df['distance_rightheelindex_anomalien'] = df['Z-Wert RHI'].apply(check_anomalien)

    right_df = df.drop(["Z-Wert Hips", "Z-Wert LKHi","Z-Wert RKHi", "Z-Wert LKHe","Z-Wert RKHe", "Z-Wert LHI", "Z-Wert RHI"], axis=1)


    #print(right_df)


    x = i.split("/")

    right_df.to_csv("model_evaluation/evaluated_distances/" + "evaluated_" + x[2], index=False)