import numpy as np
import pandas as pd
import scipy.stats as stats
import glob

# Alle Datei-Namen (.csv) in eine Liste laden
files = []
for file in glob.glob("./landmark_results_combined/*.csv"):
    files.append(file)

# Funktion, um Z-Werte einzuordnen. Rückgabewert 0 für keine Anomalie, 1 für Anomalie
def check_anomalien(z):
    # print(z)
    if z < 3:
        return 0

    else:
        return 1


# Schleife: Erstellen einer neuen CSV-Datei mit evaluierten Keypoints: Enthält Keypoints und Anomalieprüfung
for i in files:

    # Einlesen der Datei in Dataframe
    df = pd.read_csv(i)
    df = df.iloc[:, 1:]

    # Finden des absoluten Werts des Z-Werts für jedes Feature
    df["z_lefthipx"] = np.abs(stats.zscore(df["LEFT_HIP_x_back"]))
    df["z_lefthipy"] = np.abs(stats.zscore(df["LEFT_HIP_y_combined"]))
    df["z_lefthipz"] = np.abs(stats.zscore(df["LEFT_HIP_x_site"]))

    df["z_righthipx"] = np.abs(stats.zscore(df["RIGHT_HIP_x_back"]))
    df["z_righthipy"] = np.abs(stats.zscore(df["RIGHT_HIP_y_combined"]))
    df["z_righthipz"] = np.abs(stats.zscore(df["RIGHT_HIP_x_site"]))

    df["z_leftkneex"] = np.abs(stats.zscore(df["LEFT_KNEE_x_back"]))
    df["z_leftkneey"] = np.abs(stats.zscore(df["LEFT_KNEE_y_combined"]))
    df["z_leftkneez"] = np.abs(stats.zscore(df["LEFT_KNEE_x_site"]))

    df["z_rightkneex"] = np.abs(stats.zscore(df["RIGHT_KNEE_x_back"]))
    df["z_rightkneey"] = np.abs(stats.zscore(df["RIGHT_KNEE_y_combined"]))
    df["z_rightkneez"] = np.abs(stats.zscore(df["RIGHT_KNEE_x_site"]))

    df["z_leftanklex"] = np.abs(stats.zscore(df["LEFT_ANKLE_x_back"]))
    df["z_leftankley"] = np.abs(stats.zscore(df["LEFT_ANKLE_y_combined"]))
    df["z_leftanklez"] = np.abs(stats.zscore(df["LEFT_ANKLE_x_site"]))

    df["z_rightanklex"] = np.abs(stats.zscore(df["RIGHT_ANKLE_x_back"]))
    df["z_rightankley"] = np.abs(stats.zscore(df["RIGHT_ANKLE_y_combined"]))
    df["z_rightanklez"] = np.abs(stats.zscore(df["RIGHT_ANKLE_x_site"]))

    df["z_leftheelx"] = np.abs(stats.zscore(df["LEFT_HEEL_x_back"]))
    df["z_leftheely"] = np.abs(stats.zscore(df["LEFT_HEEL_y_combined"]))
    df["z_leftheelz"] = np.abs(stats.zscore(df["LEFT_HEEL_x_site"]))

    df["z_rightheelx"] = np.abs(stats.zscore(df["RIGHT_HEEL_x_back"]))
    df["z_rightheely"] = np.abs(stats.zscore(df["RIGHT_HEEL_y_combined"]))
    df["z_rightheelz"] = np.abs(stats.zscore(df["RIGHT_HEEL_x_site"]))

    df["z_leftfootindexx"] = np.abs(stats.zscore(df["LEFT_FOOT_INDEX_x_back"]))
    df["z_leftfootindexy"] = np.abs(stats.zscore(df["LEFT_FOOT_INDEX_y_combined"]))
    df["z_leftfootindexz"] = np.abs(stats.zscore(df["LEFT_FOOT_INDEX_x_site"]))

    df["z_rightfootindexx"] = np.abs(stats.zscore(df["RIGHT_FOOT_INDEX_x_back"]))
    df["z_rightfootindexy"] = np.abs(stats.zscore(df["RIGHT_FOOT_INDEX_y_combined"]))
    df["z_rightfootindexz"] = np.abs(stats.zscore(df["RIGHT_FOOT_INDEX_x_site"]))

    # Anomalien für jedes Feature überprüfen
    df["a_lefthipx"] = df["z_lefthipx"].apply(check_anomalien)
    df["a_lefthipy"] = df["z_lefthipy"].apply(check_anomalien)
    df["a_lefthipz"] = df["z_lefthipz"].apply(check_anomalien)

    df["a_righthipx"] = df["z_righthipx"].apply(check_anomalien)
    df["a_righthipy"] = df["z_righthipy"].apply(check_anomalien)
    df["a_righthipz"] = df["z_righthipz"].apply(check_anomalien)

    df["a_leftkneex"] = df["z_leftkneex"].apply(check_anomalien)
    df["a_leftkneey"] = df["z_leftkneey"].apply(check_anomalien)
    df["a_leftkneez"] = df["z_leftkneez"].apply(check_anomalien)

    df["a_rightkneex"] = df["z_rightkneex"].apply(check_anomalien)
    df["a_rightkneey"] = df["z_rightkneey"].apply(check_anomalien)
    df["a_rightkneez"] = df["z_rightkneez"].apply(check_anomalien)

    df["a_leftanklex"] = df["z_leftanklex"].apply(check_anomalien)
    df["a_leftankley"] = df["z_leftankley"].apply(check_anomalien)
    df["a_leftanklez"] = df["z_leftanklez"].apply(check_anomalien)

    df["a_rightanklex"] = df["z_rightanklex"].apply(check_anomalien)
    df["a_rightankley"] = df["z_rightankley"].apply(check_anomalien)
    df["a_rightanklez"] = df["z_rightanklez"].apply(check_anomalien)

    df["a_leftheelx"] = df["z_leftheelx"].apply(check_anomalien)
    df["a_leftheely"] = df["z_leftheely"].apply(check_anomalien)
    df["a_leftheelz"] = df["z_leftheelz"].apply(check_anomalien)

    df["a_rightheelx"] = df["z_rightheelx"].apply(check_anomalien)
    df["a_rightheely"] = df["z_rightheely"].apply(check_anomalien)
    df["a_rightheelz"] = df["z_rightheelz"].apply(check_anomalien)

    df["a_leftfootindexx"] = df["z_leftfootindexx"].apply(check_anomalien)
    df["a_leftfootindexy"] = df["z_leftfootindexy"].apply(check_anomalien)
    df["a_leftfootindexz"] = df["z_leftfootindexz"].apply(check_anomalien)

    df["a_rightfootindexx"] = df["z_rightfootindexx"].apply(check_anomalien)
    df["a_rightfootindexy"] = df["z_rightfootindexy"].apply(check_anomalien)
    df["a_rightfootindexz"] = df["z_rightfootindexz"].apply(check_anomalien)

    # Entfernen aller Z-Werte, optional
    z_columns = [
        "z_lefthipx",
        "z_lefthipy",
        "z_lefthipz",
        "z_righthipx",
        "z_righthipy",
        "z_righthipz",
        "z_leftkneex",
        "z_leftkneey",
        "z_leftkneez",
        "z_rightkneex",
        "z_rightkneey",
        "z_rightkneez",
        "z_leftanklex",
        "z_leftankley",
        "z_leftanklez",
        "z_rightanklex",
        "z_rightankley",
        "z_rightanklez",
        "z_leftheelx",
        "z_leftheely",
        "z_leftheelz",
        "z_rightheelx",
        "z_rightheely",
        "z_rightheelz",
        "z_leftfootindexx",
        "z_leftfootindexy",
        "z_leftfootindexz",
        "z_rightfootindexx",
        "z_rightfootindexy",
        "z_rightfootindexz",
    ]
    df_anomalien = df.drop(z_columns, axis=1)

    # Pfad der csv-Datei aufsplitten, benötigt für Speichern neuer Datei
    x = i.split("/")

    # Je csv-Datei erstellen einer neuen csv-Datei mit Evaluationswerten in Ordner evaluated_keypoints
    df_anomalien.to_csv(
        "model_evaluation/evaluated_keypoints/" + "evaluated_" + x[2], index=False
    )
