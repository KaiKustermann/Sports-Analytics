import pandas as pd
import os

# adjusts y coordinates of one dataframe to the other using mean
def adjust_y_coordinates(landmark_back_df, landmark_site_df):
    for column in landmark_back_df.columns:
        if column[-1:] == "y":
            df_back_column_mean = landmark_back_df[column].mean()
            df_site_column_mean = landmark_site_df[column].mean()
            delta_mean = df_back_column_mean - df_site_column_mean
            landmark_site_df[column] += delta_mean
    return landmark_back_df, landmark_site_df

# combines two dataframes (back and site video) into one dataframe using the x coordinates of back and site and combining the y coordinates to one feature using the mean
def combine_angles(landmark_back_df, landmark_site_df):
    df_combined = pd.DataFrame()
    for column in landmark_back_df.columns:
        if column[-1:] == "x":
            df_combined[column + "_back"] = landmark_back_df[column]
    for column in landmark_back_df.columns:
        if column[-1:] == "y":
            df_combined[column + "_back"] = landmark_back_df[column]
    for column in landmark_site_df.columns:
        if column[-1:] == "x":
            df_combined[column + "_site"] = landmark_site_df[column]
    for column in landmark_site_df.columns:
        if column[-1:] == "y":
            df_combined[column + "_site"] = landmark_site_df[column]

    return df_combined


def combine_back_and_side_results(directory_source: str):
    directory_in_str = directory_source
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #without .csv
        filename_edited = filename[:-4]

        if filename.endswith(".csv") and filename_edited.endswith("H_cut"):
            filename_site_edited = filename_edited[:-5] + "S_cut"
            landmark_back_df = pd.read_csv("./landmark_results/{}.csv".format(filename_edited), index_col=0)
            landmark_site_df = pd.read_csv("./landmark_results/{}.csv".format(filename_site_edited), index_col=0)
            landmark_back_df = adjust_y_coordinates(landmark_back_df, landmark_site_df)[0]
            landmark_site_df = adjust_y_coordinates(landmark_back_df, landmark_site_df)[1]
            landmark_combined_df = combine_angles(landmark_back_df, landmark_site_df)
            landmark_combined_df.to_csv("./landmark_results_combined/{}.csv".format(filename_edited[:-5] + "_combined"))
            continue
        else:
            continue