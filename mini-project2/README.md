## Read and Display Video File

This script processes video input (from a file or camera) and applies various effects based on user input. 

## Effect Implementations

### Crop Mode
```python
    frame = frame[50:400, 50:500]
```
This crops the frame to a specific region (50-400, 50-500).

### Resize Mode
```python
    frame = cv2.resize(frame, (600, 500))
```
This resizes the frame to 600x500 pixels.

### Blur Mode
```python
    frame = cv2.GaussianBlur(frame, (15, 15), 0)
```
This applies a Gaussian blur with a 15x15 kernel.

### Add a Box Mode
```python
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
```
This draws a green rectangle on the frame.

### Add Text Mode
```python
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Xinmeng Wu", (100, 100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
```
This adds blue text "Xinmeng Wu" to the frame.

### Threshold Mode
```python
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, frame = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
```
This firstly converts the color image to grayscale and applies binary thresholding to the frame and converts it back to BGR format.

### New Function Mode (Edge Detection)
```python
    edges = cv2.Canny(frame, 100, 200)
    frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
```
This applies Canny edge detection to the frame. The lower threshold (100) and upper threshold (200) control the sensitivity of edge detection.

## Usage

Run the script from the command line:
```
python WebCam.py
```
It will use the default camera.

## User Interaction

The script uses keyboard input to toggle different modes:
- 'q' or 'Q': Quit the program
- 'c' or 'C': Toggle crop mode
- 'r' or 'R': Toggle resize mode
- 'b' or 'B': Toggle blur mode
- 'a' or 'A': Toggle add a box mode
- 't' or 'T': Toggle add text mode
- 'g' or 'G': Toggle threshold mode
- 'n' or 'N': Toggle new function mode (edge detection)

Activating a new mode will automatically disable any previously active mode. 
For example, if the box mode is active and you press 'T' for text mode, the box will be removed, and the text will be displayed instead.