import pandas as pd
import plotly
import plotly.express as px
import numpy as np

# Einlesen csv-Datei
df = pd.read_csv("landmark_results_combined_new/1_Joggen_combined.csv")
df = df.iloc[:, 1:]
print(df)

# Nur Zeilen mit Column Werten unter bestimmten Wert
low_values = df.loc[df["LEFT_FOOT_INDEX_y_site"] < 0.7]
print(low_values)

# Auslesen Mindestwert einer Spalte
print(df['LEFT_FOOT_INDEX_y_site'].min())

# Auslesen Index an dem niedrigster Wert ist
index_of_min = df['LEFT_FOOT_INDEX_y_site'].idxmin()
print(index_of_min)
print(type(index_of_min))

# Winkle berechnen
b = np.array([df.LEFT_ANKLE_x_back[260], df.LEFT_ANKLE_y_back[260]])
a = np.array([df.LEFT_KNEE_x_back[260], df.LEFT_KNEE_y_back[260]])
c = np.array([df.LEFT_HEEL_x_back[260], df.LEFT_HEEL_y_back[260]])

ba = a - b
bc = c - b

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle = np.arccos(cosine_angle)

print("Winkel0: ", np.degrees(angle))

# Winkel berechnen mit Index von niedrigstem Wert
b = np.array([df.LEFT_ANKLE_x_back[index_of_min], df.LEFT_ANKLE_y_back[index_of_min]])
a = np.array([df.LEFT_KNEE_x_back[index_of_min], df.LEFT_KNEE_y_back[index_of_min]])
c = np.array([df.LEFT_HEEL_x_back[index_of_min], df.LEFT_HEEL_y_back[index_of_min]])

ba = a - b
#print(ba)
bc = c - b
#print(bc)

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle1 = np.arccos(cosine_angle)

print("Winkel1: ", np.degrees(angle1))

# Winkel berechnen mit Index niedrigster Wert plus 1
b = np.array([df.LEFT_ANKLE_x_back[index_of_min + 1], df.LEFT_ANKLE_y_back[index_of_min + 1]])
a = np.array([df.LEFT_KNEE_x_back[index_of_min + 1], df.LEFT_KNEE_y_back[index_of_min + 1]])
c = np.array([df.LEFT_HEEL_x_back[index_of_min + 1], df.LEFT_HEEL_y_back[index_of_min + 1]])

ba = a - b
#print(ba)
bc = c - b
#print(bc)

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle2 = np.arccos(cosine_angle)

print("Winkel2: ", np.degrees(angle2))

b = np.array([df.LEFT_ANKLE_x_back[263], df.LEFT_ANKLE_y_back[263]])
a = np.array([df.LEFT_KNEE_x_back[263], df.LEFT_KNEE_y_back[263]])
c = np.array([df.LEFT_HEEL_x_back[263], df.LEFT_HEEL_y_back[263]])

ba = a - b
#print(ba)
bc = c - b
#print(bc)

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle3 = np.arccos(cosine_angle)

print("Winkel3: ", np.degrees(angle3))
test = np.degrees(angle) + np.degrees(angle1) + np.degrees(angle2) + np.degrees(angle3)
test2 = test / 4



def check_class(value):
    if value <= 175:
        print("Supination")
    if value >= 185:
        print("Pronation")
    else:
        print("Neutral")

check_class(test2)