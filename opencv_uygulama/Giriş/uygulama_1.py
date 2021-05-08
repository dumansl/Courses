import cv2

img = cv2.imread("Profil.jpg",0)
cv2.imshow("Profil",img)

dugme = cv2.waitKey(0)

if dugme == 27:
    cv2.destroyAllWindows()
else :
    cv2.imwrite("C:\\Users\\User\\Desktop\\opencv\\Giriş\\griprofil.jpg",img)
    
