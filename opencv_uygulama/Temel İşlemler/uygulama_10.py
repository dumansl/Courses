import cv2
import numpy as np

img = cv2.imread("helikopter.jpg")

kuyruk = img[156:256,0:120]

img[200:300,300:420] = kuyruk

cv2.imshow("image",img)
