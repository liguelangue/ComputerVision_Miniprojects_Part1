# Xinmeng Wu 09/16/2024
import cv2
import sys
import imutils
import numpy as np

img = cv2.imread("./selfie.jpg")

if img is None:
    sys.exit("Could not read the image.")

# 1. Show Region of Interest (ROI): Define a specific region (e.g., startY=60, endY=160, startX=320, endX=420).
roi = img[900:1600, 1500:2000]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Resize Image: Adjust the image size to (200, 200).
resized = cv2.resize(img, (200, 200))
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Rotate Image: Rotate the image 45 degrees clockwise.
rotated = imutils.rotate_bound(img, 45)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Smooth Image: Apply GaussianBlur for smoothing.
smoothed_1 = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imshow("Smoothed", smoothed_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. Drawing: Draw one rectangle, one circle, and one line on the image.
drawing = img.copy()
cv2.rectangle(drawing, (250, 250), (550, 700), (255, 0, 0), 8)
cv2.circle(drawing, (750, 750), 150, (255, 0, 0), 8)
cv2.line(drawing, (1250, 1250), (2000, 2000), (255, 0, 0), 8)
cv2.imshow("Drawing", drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Add Text: Insert the text “Your Name” onto the image.
text_img = img.copy()
cv2.putText(text_img, "Xinmeng Wu", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 8)
cv2.imshow("Text", text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Convert to Grayscale: Change the image to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8. Edge Detection: Use the Canny method for edge detection
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 9. Thresholding: Apply a threshold to the image.
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 10. Detect and Draw Contours: Identify and outline the contours in the image.
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (255, 0, 0), 2)
cv2.imshow("Contours", contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()