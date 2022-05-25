import pandas as pd
import os

#only y coordinates or all coordinates????????
def adjust_y_coordinates(landmark_back_df, landmark_site_df):
    for column in landmark_back_df.columns:
        if column[-1:] == "y":
            df_back_column_mean = landmark_back_df[column].mean()
            df_site_column_mean = landmark_site_df[column].mean()
            delta_mean = df_back_column_mean - df_site_column_mean
            landmark_site_df[column] += delta_mean
    return landmark_back_df, landmark_site_df

def combine_angles(landmark_back_df, landmark_site_df, filename):
    landmark_combined_df = (landmark_back_df + landmark_site_df) / 2
    landmark_combined_df.to_csv("./landmark_results_combined/" + filename + ".csv")
    return landmark_combined_df




def combine_back_and_side_results(directory_str):
    directory_in_str = directory_str
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #without .csv
        filename_edited = filename[:-4]

        if filename.endswith(".csv") and filename_edited.endswith("H"):
            filename_site_edited = filename_edited[:-1] + "S"
            landmark_back_df = pd.read_csv("./landmark_results/{}.csv".format(filename_edited), index_col=0)
            landmark_site_df = pd.read_csv("./landmark_results/{}.csv".format(filename_site_edited), index_col=0)
            landmark_back_df = adjust_y_coordinates(landmark_back_df, landmark_site_df)[0]
            landmark_site_df = adjust_y_coordinates(landmark_back_df, landmark_site_df)[1]
            landmark_combined_df = combine_angles(landmark_back_df, landmark_site_df, filename_edited[:-1] + "_combined")
            continue
        else:
            continue