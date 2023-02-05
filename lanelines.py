#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math


def grayscale(img):

    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def canny(img, low_threshold, high_threshold):#Applies the Canny transform
    return cv2.Canny(img, low_threshold, high_threshold)


def gaussian_blur(img, kernel_size):# Applies a Gaussian Noise kernel
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices):

    # defining a blank mask to start with
    mask = np.zeros_like(img)

    # defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    # returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=2):

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)


def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):

    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def weighted_img(img, initial_img, α=0.8, β=1., γ=0.):

    return cv2.addWeighted(initial_img, α, img, β, γ)


# Import everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip
from IPython.display import HTML

def process_image(image):

    gray_image = grayscale(image)
    gaussian_image = gaussian_blur(gray_image, 3)
    canny_image = canny(gaussian_image, 150, 300)

    masked_image = region_of_interest(canny_image, np.array(
        [[(0, image.shape[0]), (500, 310), (490, 310), (image.shape[1], image.shape[0])]], dtype=np.int32))

    drawed_image = hough_lines(masked_image, 1, np.pi / 360, 50,40, 250)

    merged_image = weighted_img(drawed_image, image)
    return merged_image


clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4").subclip(0,5)
white_output = 'test_videos_output/solidWhiteRight.mp4'
white_clip = clip1.fl_image(process_image)
white_clip.write_videofile(white_output, audio=False)
