import cv2
import mediapipe as mp
import time
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

if file_path == ():
    exit()

cap = cv2.VideoCapture(file_path)

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    landmarks = results.pose_landmarks.landmark
    cv2.rectangle(img, (0,0), (1100, 1100), (0, 0, 0), -1)

    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS,
                          mpDraw.DrawingSpec(color=(245, 117, 66), thickness=3, circle_radius=3)
                          )

    # cv2.imwrite("anonym.mp4", img)
    cv2.imshow("Video", img)

    key = cv2.waitKey(1)
    if key == 27:   #ESC
        break
