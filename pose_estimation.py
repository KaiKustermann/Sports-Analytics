import cv2
import mediapipe as mp
import pandas as pd

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
points = mp_pose.PoseLandmark # Landmarks


#vor der kombination die werte korrigieren (ausreißer mithilfe graph)!!!!!!!!!!!!!!!!!!!!
#landmarks y werte auf eine höhe bringen und dann mit video seite und hinten kombinieren (durchschnitt der landmarks)

def write_landmarks_to_json(folder_path, mp4_file_name):
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

      ## Draw the pose annotation on the image.
      # image.flags.writeable = True
      # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      # mp_drawing.draw_landmarks(
      #     image,
      #     results.pose_landmarks,
      #     mp_pose.POSE_CONNECTIONS,
      #     landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

      # cv2.imshow('MediaPipe Pose', image)
      
      count = count + 1
      if cv2.waitKey(5) & 0xFF == 27:
        break

  cap.release()

  landmark_df.to_json("./landmark_results/" + mp4_file_name + ".json")


write_landmarks_to_json("assets", "Gehen-6,5-seite")