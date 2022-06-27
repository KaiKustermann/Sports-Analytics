import math
from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob
import statistics

# Einlesen Ergebnisse Fußstellung
df1 = pd.read_csv(
    "recommender/ergebnisse/results_fussstellung.csv"
)
# Einlesen Ergebnisse Fußauftritt
df2 = pd.read_csv(
    "recommender/ergebnisse/results_fussauftritt.csv"
)
# Kombinieren beider csv Dateien mit Ergebnissen, um Gesamtergebnis zu erhalten
df3 = df1.merge(df2, how='inner', on='filename')

# Endergebnis in csv-Datei speichern
df3.to_csv("recommender/ergebnisse/" + "final_results.csv", index=False)

