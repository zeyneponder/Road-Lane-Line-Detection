# Road-Lane-Line-Detection
This is a python code to detect lane lines in a video. It uses the OpenCV and moviepy libraries to process the video and identify the lane lines.

## Prerequisites

To run this code, you need to have the following libraries installed:

-OpenCV

-Numpy

-moviepy

-matplotlib

You can install these libraries using `pip` with the following commands:

```
pip install opencv-python
pip install numpy
pip install moviepy
pip install matplotlib
```

## Usage
1.Clone or download the repository.

2.Place the input video in the same folder as the code.

3.Open the terminal or command prompt and navigate to the folder containing the code.

4.Run the following command to execute the code:
```
python lanelines.py
```
The code will process the video and save the output video with the detected lane lines in the same folder.


## Configuration

You can modify the following settings in the code to customize the lane line detection:


``vertices``: The vertices of the polygon that defines the region of interest (ROI)

``region_of_interest`` function: The region of interest (ROI) to focus on the lane lines.

``canny`` function: The parameters for Canny edge detection.

``hough_lines`` function: The parameters for Hough Line Transform.


## Algorithm

The main logic of the lane line detection process can be broken down into the following steps:

**Load the video**: Use the moviepy library to load the video file and process each frame.

**Pre-processing**: Convert the frame from color to grayscale, and apply Gaussian blur to reduce noise and increase the signal-to-noise ratio.

**Edge detection**: Use the Canny edge detection algorithm to identify edges in the image.

**Masking**: Apply a mask to focus only on the region of interest (ROI) where the lane lines are expected to be.

**Hough Line Transform**: Use the Hough Line Transform to identify the lines in the image.

**Line Segmentation**: Segment the lines into left and right lane lines based on their slope and location in the image.


**Overlay**: Overlay the detected lane lines on the original image, and display the result.
