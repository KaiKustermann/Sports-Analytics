import numpy as np
import pandas as pd
import scipy.stats as stats
import glob


# Berechnung der Distanz zwischen Hüft-Keypoints
def calculate_hip_distance(i):
    #print(i)
    p1 = np.array([filtered_csv.LEFT_HIP_x_back[i], filtered_csv.LEFT_HIP_y_combined[i], filtered_csv.LEFT_HIP_x_site[i]])
    p2 = np.array([filtered_csv.RIGHT_HIP_x_back[i], filtered_csv.RIGHT_HIP_y_combined[i], filtered_csv.RIGHT_HIP_x_site[i]])

    dist = np.linalg.norm(p1 - p2)
    #print("Hip Distance:", dist)
    return dist


# Berechnung der Distanz zwischen Knie und Hüfte links
def calculate_left_kneehip_distance(i):
    p3 = np.array([filtered_csv.LEFT_HIP_x_back[i], filtered_csv.LEFT_HIP_y_combined[i], filtered_csv.LEFT_HIP_x_site[i]])
    p4 = np.array([filtered_csv.LEFT_KNEE_x_back[i], filtered_csv.LEFT_KNEE_y_combined[i], filtered_csv.LEFT_KNEE_x_site[i]])

    dist = np.linalg.norm(p3 - p4)
    #print("Left Hip-Knee Distance:", dist)
    return dist


# Berechnung der Distanz zwischen Knie und Hüfte rechts
def calculate_right_kneehip_distance(i):
    p5 = np.array([filtered_csv.RIGHT_HIP_x_back[i], filtered_csv.RIGHT_HIP_y_combined[i], filtered_csv.RIGHT_HIP_x_site[i]])
    p6 = np.array([filtered_csv.RIGHT_KNEE_x_back[i], filtered_csv.RIGHT_KNEE_y_combined[i], filtered_csv.RIGHT_KNEE_x_site[i]])

    dist = np.linalg.norm(p5 - p6)
    #print("Right Hip-Knee Distance:", dist)
    return dist

# Berechnung der Distanz zwischen Knie und Knöchel links
def calculate_left_kneeankle_distance(i):
    p7 = np.array([filtered_csv.LEFT_KNEE_x_back[i], filtered_csv.LEFT_KNEE_y_combined[i], filtered_csv.LEFT_KNEE_x_site[i]])
    p8 = np.array([filtered_csv.LEFT_ANKLE_x_back[i], filtered_csv.LEFT_ANKLE_y_combined[i], filtered_csv.LEFT_ANKLE_x_site[i]])

    dist = np.linalg.norm(p7 - p8)
    #print("Left Knee-Ankle Distance:", dist)
    return dist


# Berechnung der Distanz zwischen Knie und Knöchel rechts
def calculate_right_kneeankle_distance(i):
    p9 = np.array([filtered_csv.RIGHT_KNEE_x_back[i], filtered_csv.RIGHT_KNEE_y_combined[i], filtered_csv.RIGHT_KNEE_x_site[i]])
    p10 = np.array([filtered_csv.RIGHT_ANKLE_x_back[i], filtered_csv.RIGHT_ANKLE_y_combined[i], filtered_csv.RIGHT_ANKLE_x_site[i]])

    dist = np.linalg.norm(p9 - p10)
    #print("Right Knee-Ankle Distance:", dist)
    return dist

# Berechnung der Distanz zwischen Knie und Ferse links
def calculate_left_kneeheel_distance(i):
    p11 = np.array([filtered_csv.LEFT_KNEE_x_back[i], filtered_csv.LEFT_KNEE_y_combined[i], filtered_csv.LEFT_KNEE_x_site[i]])
    p12 = np.array([filtered_csv.LEFT_HEEL_x_back[i], filtered_csv.LEFT_HEEL_y_combined[i], filtered_csv.LEFT_HEEL_x_site[i]])

    dist = np.linalg.norm(p11 - p12)
    #print("Left Knee-Ankle Distance:", dist)
    return dist


# Berechnung der Distanz zwischen Knie und Ferse rechts
def calculate_right_kneeheel_distance(i):
    p13 = np.array([filtered_csv.RIGHT_KNEE_x_back[i], filtered_csv.RIGHT_KNEE_y_combined[i], filtered_csv.RIGHT_KNEE_x_site[i]])
    p14 = np.array([filtered_csv.RIGHT_HEEL_x_back[i], filtered_csv.RIGHT_HEEL_y_combined[i], filtered_csv.RIGHT_HEEL_x_site[i]])

    dist = np.linalg.norm(p13 - p14)
    #print("Right Knee-Ankle Distance:", dist)
    return dist

# Berechnung der Distanz zwischen Knöchel und Fußspitze links
def calculate_left_ankleindex_distance(i):
    p15 = np.array([filtered_csv.LEFT_ANKLE_x_back[i], filtered_csv.LEFT_ANKLE_y_combined[i], filtered_csv.LEFT_ANKLE_x_site[i]])
    p16 = np.array([filtered_csv.LEFT_FOOT_INDEX_x_back[i], filtered_csv.LEFT_FOOT_INDEX_y_combined[i], filtered_csv.LEFT_FOOT_INDEX_x_site[i]])

    dist = np.linalg.norm(p15 - p16)
    #print("Left Ankle-Footindex Distance:", dist)
    return dist


# Berechnung der Distanz zwischen Knöchel und Fußspitze rechts
def calculate_right_ankleindex_distance(i):
    p17 = np.array([filtered_csv.RIGHT_ANKLE_x_back[i], filtered_csv.RIGHT_ANKLE_y_combined[i], filtered_csv.RIGHT_ANKLE_x_site[i]])
    p18 = np.array([filtered_csv.RIGHT_FOOT_INDEX_x_back[i], filtered_csv.RIGHT_FOOT_INDEX_y_combined[i], filtered_csv.RIGHT_FOOT_INDEX_x_site[i]])

    dist = np.linalg.norm(p17 - p18)
    #print("Right Ankle-Footindex:", dist)
    return dist

# Berechnung der Distanz zwischen Ferse und Fußspitze links
def calculate_left_heelindex_distance(i):
    p19 = np.array([filtered_csv.LEFT_HEEL_x_back[i], filtered_csv.LEFT_HEEL_y_combined[i], filtered_csv.LEFT_HEEL_x_site[i]])
    p20 = np.array([filtered_csv.LEFT_FOOT_INDEX_x_back[i], filtered_csv.LEFT_FOOT_INDEX_y_combined[i], filtered_csv.LEFT_FOOT_INDEX_x_site[i]])

    dist = np.linalg.norm(p19 - p20)
    #print("Left Foot Distance:", dist)
    return dist


# Berechnung der Distanz zwischen Ferse und Fußspitze rechts
def calculate_right_heelindex_distance(i):
    p21 = np.array([filtered_csv.RIGHT_HEEL_x_back[i], filtered_csv.RIGHT_HEEL_y_combined[i], filtered_csv.RIGHT_HEEL_x_site[i]])
    p22 = np.array([filtered_csv.RIGHT_FOOT_INDEX_x_back[i], filtered_csv.RIGHT_FOOT_INDEX_y_combined[i], filtered_csv.RIGHT_FOOT_INDEX_x_site[i]])

    dist = np.linalg.norm(p21 - p22)
    #print("Right Foot Distance:", dist)
    return dist



# Alle Datei-Namen (.csv) in eine Liste laden
files = []
for file in glob.glob("./landmark_results_combined/*.csv"):
    files.append(file)

# Erstellen einer neuen CSV-Datei mit Distanzen für jede CSV-Datei mit Keypoints

for i in files:
    # Einlesen der Datei in Dataframe
    filtered_csv = pd.read_csv(i)

    # Berechnung der Hüft-Distanz pro Reihe, Speichern in neuer Series
    new_df = filtered_csv.apply(lambda row: calculate_hip_distance(row.name), axis=1, result_type="expand")

    # Umwandlung Series zu Dataframe mit Spaltenname
    new_df = pd.DataFrame({'distance_hips': new_df.values})

    # Berechnung aller anderen Distanzen und hinzufügen zu Dataframe
    new_df['distance_leftkneehip'] = filtered_csv.apply(lambda row: calculate_left_kneehip_distance(row.name),
                                                            axis=1)
    new_df['distance_rightkneehip'] = filtered_csv.apply(lambda row: calculate_right_kneehip_distance(row.name),
                                                             axis=1)

    new_df['distance_leftkneeankle'] = filtered_csv.apply(lambda row: calculate_left_kneeankle_distance(row.name),
                                                             axis=1)
    new_df['distance_rightkneeankle'] = filtered_csv.apply(lambda row: calculate_right_kneeankle_distance(row.name),
                                                              axis=1)

    new_df['distance_leftkneeheel'] = filtered_csv.apply(lambda row: calculate_left_kneeheel_distance(row.name),
                                                             axis=1)
    new_df['distance_rightkneeheel'] = filtered_csv.apply(lambda row: calculate_right_kneeheel_distance(row.name),
                                                              axis=1)

    new_df['distance_leftankleindex'] = filtered_csv.apply(lambda row: calculate_left_ankleindex_distance(row.name),
                                                              axis=1)
    new_df['distance_rightankleindex'] = filtered_csv.apply(lambda row: calculate_right_ankleindex_distance(row.name),
                                                               axis=1)

    new_df['distance_leftheelindex'] = filtered_csv.apply(lambda row: calculate_left_heelindex_distance(row.name),
                                                              axis=1)
    new_df['distance_rightheelindex'] = filtered_csv.apply(lambda row: calculate_right_heelindex_distance(row.name),
                                                               axis=1)


    # Dateinamen extrahieren
    x = i.split("/")

    # Dataframe in neue CSV in Ordner distances speichern
    new_df.to_csv("model_evaluation/distances/" + "distances_" + x[2], index=False)