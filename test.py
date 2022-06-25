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
