import cv2
import numpy as np

img = cv2.imread("helikopter.jpg")
img1 = cv2.imread("helikopter2.jpg")


img2 = img1[285:697,320:960]

dst = cv2.addWeighted(img,0.6,img2,0.4,0)

cv2.imshow("dst",dst)
