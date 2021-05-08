import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.rectangle(img , (0,0),(100,100),(100,0,0),3)

cv2.imshow("img",img)
