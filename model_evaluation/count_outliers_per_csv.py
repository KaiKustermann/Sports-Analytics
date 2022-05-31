import pandas as pd
import glob

files = []
for file in glob.glob("model_evaluation/evaluated_distances/*.csv"):
    files.append(file)

#Zählen der Ausreißer-Werte je Feature und je Datei für DISTANZEN
for i in files:
    # Einlesen der Datei in Dataframe
    df = pd.read_csv(i)

    # Auftrennen Dateipfad um Dateiname zu extrahieren
    x = i.split("/")

    # Zählen der Anomalien (Wert 1) je Feature
    count_dist_hips = len(df[df.distance_hips_anomalien == 1])
    print("Anzahl Anomalien für Distanz Hüfte:", count_dist_hips)

    count_dist_leftkneehip = len(df[df.distance_leftkneehips_anomalien == 1])
    print("Anzahl Anomalien für Distanz Knie-Hüfte links:", count_dist_leftkneehip)

    count_dist_rightkneehip = len(df[df.distance_rightkneehips_anomalien == 1])
    print("Anzahl Anomalien für Distanz Knie-Hüfte rechts:", count_dist_rightkneehip)

    count_dist_leftkneeheel = len(df[df.distance_leftkneeheel_anomalien == 1])
    print("Anzahl Anomalien für Distanz Knie-Ferse links:", count_dist_leftkneeheel)

    count_dist_rightkneeheel = len(df[df.distance_rightkneeheel_anomalien == 1])
    print("Anzahl Anomalien für Distanz Knie-Ferse rechts:", count_dist_rightkneeheel)

    count_dist_leftkneeankle = len(df[df.distance_leftkneeankle_anomalien == 1])
    print("Anzahl Anomalien für Distanz Knie-Knöchel links:", count_dist_leftkneeankle)

    count_dist_rightkneeankle = len(df[df.distance_rightkneeankle_anomalien == 1])
    print(
        "Anzahl Anomalien für Distanz Knie-Knöchel rechts:", count_dist_rightkneeankle
    )

    count_dist_leftheelindex = len(df[df.distance_leftheelindex_anomalien == 1])
    print(
        "Anzahl Anomalien für Distanz Ferse-Fußspitze links:", count_dist_leftheelindex
    )

    count_dist_rightheelindex = len(df[df.distance_rightheelindex_anomalien == 1])
    print(
        "Anzahl Anomalien für Distanz Ferse-Fußspitze rechts:",
        count_dist_rightheelindex,
    )

    count_dist_leftankleindex = len(df[df.distance_leftankleindex_anomalien == 1])
    print(
        "Anzahl Anomalien für Distanz Knöchel-Fußspitze links:",
        count_dist_leftankleindex,
    )

    count_dist_rightankleindex = len(df[df.distance_rightankleindex_anomalien == 1])
    print(
        "Anzahl Anomalien für Distanz Knöchel-Fußspitze rechts:",
        count_dist_rightankleindex,
    )

    # Werte zusammenzählen
    count_anomalies = (
        count_dist_hips
        + count_dist_leftkneehip
        + count_dist_rightkneehip
        + count_dist_leftkneeheel
        + count_dist_rightkneeheel
        + count_dist_leftkneeankle
        + count_dist_rightkneeankle
        + count_dist_leftheelindex
        + count_dist_rightheelindex
        + count_dist_leftankleindex
        + count_dist_rightankleindex
    )
    print("Es gibt insgesamt", count_anomalies, "Ausreißer in Datei", x[2])
