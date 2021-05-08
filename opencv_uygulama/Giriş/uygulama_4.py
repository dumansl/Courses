import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.line(img,(0,0),(360,480),(100,0,0),5)

cv2.imshow("img",img)
