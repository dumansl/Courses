import cv2

yVid = cv2.VideoCapture("sokak.mp4")

while True :
    deger,kare=yVid.read()
    cv2.imshow("sokak2",kare)
    if cv2.waitKey(1) & 0xFF == ord("a") :
        break
yVid.release()
cv2.destroyAllWindows()
