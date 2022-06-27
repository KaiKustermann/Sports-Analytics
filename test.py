import math
from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob
import statistics

df = pd.read_csv(
    "landmark_results_combined_new/4_Joggen_combined.csv"
)
lookahead= 13
df=df.iloc[:, 1:]
relevant_column = df["LEFT_HEEL_y_site"]
peaks = peakdetect(relevant_column, lookahead=lookahead)

lowerPeaks = np.array(peaks[1])
df = pd.DataFrame(lowerPeaks, columns = ['old_index','value'])
print(df)
indices = lowerPeaks[:,0]
values = lowerPeaks[:,1]
#print(lowerPeaks)
#print(values)


sorted_df = df.sort_values(by=['value'], ignore_index=True)
print(sorted_df)
median = statistics.median_low(sorted_df["value"])
print(median)
test = sorted_df.index[sorted_df['value'] == median].tolist()


neue_liste = sorted_df.iloc[test[0] - 10 : test[0] + 10]
print(neue_liste)
liste = neue_liste['old_index'].tolist()
print(liste)

def calculate_angle(x1, x2, y1, y2):
    print(x1, y1)
    print(x2, y2)
    delta_y = ((y2) - (y1)) ** 2
    delta_x = ((x2) - (x1)) ** 2
    radian = math.atan2(delta_y, delta_x)
    degrees = radian * (180 / math.pi)
    return degrees

def culculate_metric(df, frame, img):
    foot_index_x, foot_index_y = df.iloc[frame]["32z"], df.iloc[frame]["32y"]
    heel_x, heel_y = df.iloc[frame]["30z"], df.iloc[frame]["30y"]
    angle = calculate_angle(foot_index_x, heel_x, foot_index_y, heel_y)

    """ 
    # adjust coordinates to screen resolution
    # use only this block OR the block above
    h, w, c = img.shape
    foot_index_x_adjusted, foot_index_y_adjusted = int(foot_index_x*w), int(foot_index_y*h)
    heel_x_adjusted, heel_y_adjusted = int(heel_x*w), int(heel_y*h)
    angle = calculate_angle(foot_index_x_adjusted, heel_x_adjusted, foot_index_y_adjusted, heel_y_adjusted) 
    """

    print(angle)
    row = ['', angle] 
    return row

def get_change(current, previous):
    if current == previous:
        return 0
    try:
        print((abs(current - previous) / previous) * 100.0)
    except ZeroDivisionError:
        return float('inf')

def get_change2(current, previous):
    if current == previous:
        return 0
    try:
        print(current - previous)
    except ZeroDivisionError:
        return float('inf')

get_change(0.747, 0.789)
get_change(0.789, 0.747)

get_change2(0.747, 0.789)
get_change2(0.789, 0.747)