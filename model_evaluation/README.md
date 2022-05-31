### READ ME ###

Bitte beachten, um die Model Evaluation ohne Probleme auszuführen:

Voraussetzung:
1. Ordner "landmark_results_combined" muss befüllt sein
2. Alle packages importiert:
    - pandas
    - plotly
    - plotly.express
    - glob
    - scipy.stats
    - numpy
3. Ordner "distances", "evaluated_distances" und "evaluated_keypoints" müssen im Ordner "model_evaluation" LEER vorhanden sein


Empfohlene Reihenfolge der auszuführenden Files, wobei 1 vor 2 ausgeführt werden MUSS:
1. create_distances.py
2. evaluate_distances.py
3. evaluate_all_keypoints.py
4. visualize_evaluation.py

Bitte vom Gesamtordner aus starten, da sonst Pfade nicht gefunden werden können.