import math
from peakdetect import peakdetect
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import glob
import statistics

def combine_results():
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

    df4 = pd.read_csv(
        "recommender/ergebnisse/results_fussstellung_adjusted.csv"
    )

    df5 = df3.merge(df4, how='inner', on='filename')
    # Endergebnis in csv-Datei speichern
    df5.to_csv("recommender/ergebnisse/" + "final_results.csv", index=False)

