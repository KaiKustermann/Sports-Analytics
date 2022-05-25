from back_and_side_combination import combine_back_and_side_results
from mov_to_mp4 import mov_to_mp4
import os
from pose_estimation import save_landmarks_of_videos
from video_editing import extract_subclips_from_videos


# convert mov to mp4 (prerequisit: ffmpeg must be installed)
mov_to_mp4("J:/Kai Kustermann/HDM/Semester 7/Sports Analytics/mp4_2/mp4_2/")


# edit all videos, so that it extracts a subclip from the video, which starts at the loudest point (eg. clap) and lasts one minute
# we did that manually because the results where not accurate
extract_subclips_from_videos("J:/Kai Kustermann/HDM/Semester 7/Sports Analytics/mp4_2/mp4_2/")


# save landmarks of the pose estimation results in a csv in the folder landmark_results
save_landmarks_of_videos("J:/Kai Kustermann/HDM/Semester 7/Sports Analytics/mp4_2/mp4_2/")


# combine the results of back and side by adjusting the y coordinate and taking the mean of the two results
combine_back_and_side_results("./landmark_results")





