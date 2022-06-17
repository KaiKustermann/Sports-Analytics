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

for x in files:

    df = pd.read_csv(x)
    df = df.iloc[:, 1:]

    relevant_column = df["LEFT_FOOT_INDEX_y_site"]

    peaks = peakdetect(relevant_column, lookahead=15)

    lowerPeaks = np.array(peaks[1])
    indices = lowerPeaks[:,0]

    #plt.plot(testdata)
    #plt.plot(lowerPeaks[:,0], lowerPeaks[:,1], 'ko')
    #plt.show()

    mittelwert = []
    test_mw = 0
    count = 0

    for i in indices:

        # Winkle berechnen
        b = np.array([df.LEFT_ANKLE_x_back[i], df.LEFT_ANKLE_y_back[i]])
        a = np.array([df.LEFT_KNEE_x_back[i], df.LEFT_KNEE_y_back[i]])
        c = np.array([df.LEFT_HEEL_x_back[i], df.LEFT_HEEL_y_back[i]])

        ba = a - b
        bc = c - b

        cosine_angle1 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle1 = np.arccos(cosine_angle1)

        #print("Winkel1 von", i , np.degrees(angle1))
        winkel = np.degrees(angle1)
        mittelwert.append(np.degrees(angle1))
        test_mw = test_mw + np.degrees(angle1)
        count = count + 1

    angle_file = (test_mw / count)

    checkup = check_class(angle_file)
    print("For file", x, "class:", checkup)

    break
