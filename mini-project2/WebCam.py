# Xinmeng Wu 09/16/24
# USAGE: python WebCam.py

# import the necessary packages
import cv2
import numpy as np
import time
import os
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Video file path or camera input")
parser.add_argument("-f", "--file", type=str, help="Path to the video file")
args = parser.parse_args()

# Check if the file argument is provided, otherwise use the camera
if args.file:
    vs = cv2.VideoCapture(args.file)
else:
    vs = cv2.VideoCapture(0)  # 0 is the default camera

time.sleep(1.0)

active_mode = None

# loop over the frames from the video stream
while True:
    # Reset video to the beginning if it's at the end
    if vs.get(cv2.CAP_PROP_POS_FRAMES) == vs.get(cv2.CAP_PROP_FRAME_COUNT):
        vs.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    # grab the frame from video stream
    ret, frame = vs.read()
    if not ret:
        continue

    # Add your code HERE: For example,
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if active_mode == 'crop':
        frame = frame[50:400, 50:500]
    elif active_mode == 'resize':
        frame = cv2.resize(frame, (600, 500))
    elif active_mode == 'blur':
        frame = cv2.GaussianBlur(frame, (15, 15), 0)
    elif active_mode == 'box':
        cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
    elif active_mode == 'text':
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Xinmeng Wu", (100, 100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
    elif active_mode == 'threshold':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, frame = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    elif active_mode == 'new_function': # edge detection
        edges = cv2.Canny(frame, 100, 200)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    elif key == ord('c') or key == ord('C'):
        active_mode = 'crop' if active_mode != 'crop' else None
    elif key == ord('r') or key == ord('R'):
        active_mode = 'resize' if active_mode != 'resize' else None
    elif key == ord('b') or key == ord('B'):
        active_mode = 'blur' if active_mode != 'blur' else None
    elif key == ord('a') or key == ord('A'):
        active_mode = 'box' if active_mode != 'box' else None
    elif key == ord('t') or key == ord('T'):
        active_mode = 'text' if active_mode != 'text' else None
    elif key == ord('g') or key == ord('G'):
        active_mode = 'threshold' if active_mode != 'threshold' else None
    elif key == ord('n') or key == ord('N'):
        active_mode = 'new_function' if active_mode != 'new_function' else None

cv2.destroyAllWindows()
vs.release()
