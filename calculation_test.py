from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob

df = pd.read_csv(
    "landmark_results_combined_new/2_Joggen_combined.csv"
)

df=df.iloc[:, 1:]
i = 99
x = 0

# Version 1
b = np.array([df.LEFT_ANKLE_x_back[i+x], df.LEFT_ANKLE_y_back[i+x]])
a = np.array([df.LEFT_KNEE_x_back[i+x], df.LEFT_KNEE_y_back[i+x]])
c = np.array([df.LEFT_HEEL_x_back[i+x], df.LEFT_HEEL_y_back[i+x]])

ba = a - b
bc = c - b

print(ba)
print(bc)

unit_vector_1 = ba / np.linalg.norm(ba)
unit_vector_2 = bc / np.linalg.norm(bc)
dot_product = np.dot(unit_vector_1, unit_vector_2)
angle = np.arccos(dot_product)

print(angle)
print(np.degrees(angle))

# Version 2, gleiches Ergebnis
p0 = np.array([df.LEFT_KNEE_x_back[i+x], df.LEFT_KNEE_y_back[i+x]])
p1 = np.array([df.LEFT_ANKLE_x_back[i+x], df.LEFT_ANKLE_y_back[i+x]])
p2 = np.array([df.LEFT_HEEL_x_back[i+x], df.LEFT_HEEL_y_back[i+x]])
''' 
compute angle (in degrees) for p0p1p2 corner
Inputs:
    p0,p1,p2 - points in the form of [x,y]
'''

v0 = np.array(p0) - np.array(p1)
v1 = np.array(p2) - np.array(p1)

angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
print(np.degrees(angle))
    