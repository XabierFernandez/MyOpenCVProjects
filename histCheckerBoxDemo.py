import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt



# Read the image.
img = cv2.imread('./module03-histograms-and-color-segmentation/checkerboard_18x18.png', cv2.IMREAD_GRAYSCALE)

# Flatten the image data into a single 1D array.
img_flatten = img.ravel()

# Display the image and histograms.
plt.figure(figsize = [18, 4])

plt.subplot(131); plt.imshow(img); plt.title('Original Image')

plt.subplot(132) 
plt.hist(img_flatten, 5, [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pixels')
plt.title('5 Bins')

plt.subplot(133)
plt.hist(img_flatten, 50, [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pi')
plt.title('50 Bins')