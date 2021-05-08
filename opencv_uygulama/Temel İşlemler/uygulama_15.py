import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread ("median.png")
img_bilateral = cv2.imread ("bilateral.png")

blur = cv2.blur(img_filter,(7,7))
blur2= cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)
blur3= cv2.medianBlur(img_median,9)
blur4= cv2.bilateralFilter(img_bilateral,9,75,75)


cv2.imshow("img",img_median)
cv2.imshow("blur3",blur3)



cv2.waitKey(0)
cv2.destroyAllWindows()
