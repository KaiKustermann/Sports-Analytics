import pandas as pd
import plotly
import plotly.express as px

df = pd.read_csv("landmark_results_combined_new/1_Joggen_combined.csv")

df2 = df.iloc[645]
print(df2)