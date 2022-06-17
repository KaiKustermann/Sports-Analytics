from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

df = pd.read_csv("landmark_results_combined_new/1_Joggen_combined.csv")
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

    print("Winkel1 von", i , np.degrees(angle1))
    mittelwert.append(np.degrees(angle1))
    test_mw = test_mw + np.degrees(angle1)
    count = count + 1

    b = np.array([df.LEFT_ANKLE_x_back[i+1], df.LEFT_ANKLE_y_back[i+1]])
    a = np.array([df.LEFT_KNEE_x_back[i+1], df.LEFT_KNEE_y_back[i+1]])
    c = np.array([df.LEFT_HEEL_x_back[i+1], df.LEFT_HEEL_y_back[i+1]])

    ba = a - b
    bc = c - b

    cosine_angle2 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle2 = np.arccos(cosine_angle2)

    print("Winkel2 von", i , np.degrees(angle2))

    break




print(mittelwert)
print(test_mw)
print(count)
print(test_mw / count)

def check_class(value):
    if value <= 175:
        print("Supination")
    if value >= 185:
        print("Pronation")
    else:
        print("Neutral")


# Winkle berechnen
b = np.array([df.LEFT_ANKLE_x_back[32], df.LEFT_ANKLE_y_back[32]])
a = np.array([df.LEFT_KNEE_x_back[32], df.LEFT_KNEE_y_back[32]])
c = np.array([df.LEFT_HEEL_x_back[32], df.LEFT_HEEL_y_back[32]])

ba = a - b
bc = c - b

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle = np.arccos(cosine_angle)

print("Winkel von 32" , np.degrees(angle))