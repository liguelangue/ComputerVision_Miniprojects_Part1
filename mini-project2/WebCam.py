# Xinmeng Wu 09/16/24
# USAGE: python WebCam.py -f video_file_name

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

# Initialize variables for different effects
crop_mode = False
resize_mode = False
blur_mode = False
box_mode = False
text_mode = False
threshold_mode = False
new_function_mode = False

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
    if crop_mode:
        frame = frame[50:400, 50:500]
    
    if resize_mode:
        frame = cv2.resize(frame, (600, 500))
    
    if blur_mode:
        frame = cv2.GaussianBlur(frame, (15, 15), 0)
    
    if box_mode:
        cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
    
    if text_mode:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Xinmeng Wu", (100, 100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    if threshold_mode:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, frame = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        # single-channel to three-channel
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    
    # New function (edge detection)
    if new_function_mode:
        edges = cv2.Canny(frame, 100, 200)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    elif key == ord('c') or key == ord('C'):
        crop_mode = not crop_mode
    elif key == ord('r') or key == ord('R'):
        resize_mode = not resize_mode
    elif key == ord('b') or key == ord('B'):
        blur_mode = not blur_mode
    elif key == ord('a') or key == ord('A'):
        box_mode = not box_mode
    elif key == ord('t') or key == ord('T'):
        text_mode = not text_mode
    elif key == ord('g') or key == ord('G'):
        threshold_mode = not threshold_mode
    elif key == ord('n') or key == ord('N'):
        new_function_mode = not new_function_mode

cv2.destroyAllWindows()
vs.release()
