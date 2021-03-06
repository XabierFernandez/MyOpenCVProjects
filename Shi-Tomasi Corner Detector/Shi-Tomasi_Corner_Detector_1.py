import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

filename = '../data/blox.jpg'

img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray,25,0.010,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)

cv.imshow('ret',img)
cv.waitKey(0)
cv.destroyAllWindows()