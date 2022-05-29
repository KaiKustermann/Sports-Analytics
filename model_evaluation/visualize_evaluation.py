import pandas as pd
import plotly
import plotly.express as px

df = pd.read_csv("model_evaluation/evaluated_distances/evaluated_distances_7_Joggen_combined.csv")

fig1= px.line(df, x=df.index, y=['distance_leftkneehip', 'distance_leftkneehips_anomalien'], title='Anomalien Hüfte - Knie links')
fig1.show()








