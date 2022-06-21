from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob

def check_class(value):
    if value <= 175:
        return "Supination"
    if value >= 185:
        return "Pronation"
    else:
        return "Neutral"

files = []
for file in glob.glob("landmark_results_combined_new/*.csv"):
    files.append(file)

for y in files:

    df = pd.read_csv(y)
    df = df.iloc[:, 1:]

    relevant_column = df["LEFT_HEEL_y_site"]

    #Extrahieren der Geschwindigkeit aus Name der csv Datei
    video = y.split("/")
    video_splitted  = video[1]
    z = video_splitted.split("_")
    speed = z[1]

    #Lookahead je nach Geschwindigkeit anpassen
    if speed == "Joggen":
        lookahead = 13
        frame = 3
    if speed == "Laufen":
        lookahead = 13
        frame = 2
    if speed == "Gehen":
        lookahead = 15
        frame = 4

    peaks = peakdetect(relevant_column, lookahead=lookahead)

    lowerPeaks = np.array(peaks[1])
    indices = lowerPeaks[:,0]
    mittelwert = []
    test_mw = 0
    count = 0
    #print(speed)

    # Alle Indizes der Tiefpunkte durchgehen
    for i in indices:
        #print(i)

        # Liste für Anzahl extra Frames nach links und rechts machen
        extra_frames = list(range(0, frame+1, 1))
        count_per_cyclus = 0
        mw_per_cyclus = 0

        # Für Zahlen in Liste extra Frames: Jedes zu Index addieren und Winkel berechnen
        for x in extra_frames:
            # Winkle berechnen
            count_per_cyclus = count_per_cyclus + 2

            b = np.array([df.LEFT_ANKLE_x_back[i+x], df.LEFT_ANKLE_y_back[i+x]])
            a = np.array([df.LEFT_KNEE_x_back[i+x], df.LEFT_KNEE_y_back[i+x]])
            c = np.array([df.LEFT_HEEL_x_back[i+x], df.LEFT_HEEL_y_back[i+x]])

            ba = a - b
            bc = c - b

            cosine_angle1 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
            angle1 = np.arccos(cosine_angle1)

            #print("Winkel1 von", i+x , np.degrees(angle1))
            mw_per_cyclus = mw_per_cyclus + np.degrees(angle1)

            b = np.array([df.LEFT_ANKLE_x_back[i-x], df.LEFT_ANKLE_y_back[i-x]])
            a = np.array([df.LEFT_KNEE_x_back[i-x], df.LEFT_KNEE_y_back[i-x]])
            c = np.array([df.LEFT_HEEL_x_back[i-x], df.LEFT_HEEL_y_back[i-x]])

            ba = a - b
            bc = c - b

            cosine_angle2 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
            angle2 = np.arccos(cosine_angle2)

            #print("Winkel1 von", i+x , np.degrees(angle1))
            mw_per_cyclus = mw_per_cyclus + np.degrees(angle2)
        
        angle_cyclus = (mw_per_cyclus / count_per_cyclus) 
        print(angle_cyclus)   
        #winkel = np.degrees(angle1)
        #mittelwert.append(np.degrees(angle1))
        test_mw = test_mw + np.degrees(angle1)
        count = count + 1
  
    angle_file = (test_mw / count)
    print("Winkel: ", angle_file)
    checkup = check_class(angle_file)
    print("For file", y, "class:", checkup)
    break



