import cv2
import mediapipe as mp
import pandas as pd
import os

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
points = mp_pose.PoseLandmark # Landmarks


#vor der kombination die werte korrigieren (ausreißer mithilfe graph)!!!!!!!!!!!!!!!!!!!!
#landmarks y werte auf eine höhe bringen und dann mit video seite und hinten kombinieren (durchschnitt der landmarks)

def write_landmarks_to_csv(folder_path, mp4_file_name):
  cap = cv2.VideoCapture(folder_path + "/" + mp4_file_name + ".mp4")
  count = 0

  data = []
  for p in points:
          x = str(p)[13:]
          data.append(x + "_x")
          data.append(x + "_y")
          data.append(x + "_z")
          data.append(x + "_vis")
  landmark_df = pd.DataFrame(columns = data) # Empty dataset

  with mp_pose.Pose(
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        break

      # To improve performance, optionally mark the image as not writeable
      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = pose.process(image)

      landmarks = []
      i = 0
      for landmark in results.pose_landmarks.landmark:
        landmarks.append(landmark.x)
        landmarks.append(landmark.y)
        landmarks.append(landmark.z)
        landmarks.append(landmark.visibility)
        i += 1

      landmark_df.loc[len(landmark_df)] = landmarks

      if count == 1:
        print(landmark_df)
      
      count = count + 1
      if cv2.waitKey(5) & 0xFF == 27:
        break

  cap.release()

  #slice from the first column that we need (from hip onwards)
  landmark_df = landmark_df.loc[:, 'LEFT_HIP_x':]
  landmark_df.to_csv("./landmark_results/" + mp4_file_name + ".csv")


def save_landmarks_of_videos(directory_str):
  directory_in_str = directory_str
  directory = os.fsencode(directory_in_str)

  for file in os.listdir(directory):
      filename = os.fsdecode(file)
      filename = filename[:-4]
      if (filename.endswith("_cut")): 
          write_landmarks_to_csv(directory_in_str, filename)
          continue
      else:
          continue

