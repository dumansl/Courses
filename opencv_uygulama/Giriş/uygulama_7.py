import cv2
import numpy as np

def bos(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("image")



cv2.createTrackbar("R","image",0,255,bos)
cv2.createTrackbar("G","image",0,255,bos)
cv2.createTrackbar("B","image",0,255,bos)
cv2.createTrackbar("On-Off","image",0,1,bos)



while(1):
    cv2.imshow("image",img)
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
    r= cv2.getTrackbarPos("R","image")
    g= cv2.getTrackbarPos("G","image")
    b= cv2.getTrackbarPos("B","image")
    s= cv2.getTrackbarPos("On-Off","image")
    if s== 1 :
        img[:] =[b,g,r]
    else:
        img[:]=[0]

cv2.destroyAllWindows()
        
