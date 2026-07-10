import cv2
import numpy as np 

framewidth=640
frameHeight=480

cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameHeight)

def  empty(a):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,240)
cv2.createTrackbar("HUE min",'Trackbar',0,179,empty)
cv2.createTrackbar("HUE max",'Trackbar',179,179,empty)
cv2.createTrackbar("SAT min",'Trackbar',0,255,empty)
cv2.createTrackbar("SAT max",'Trackbar',255,255,empty)
cv2.createTrackbar("VAL min",'Trackbar',0,255,empty)
cv2.createTrackbar("VAL max",'Trackbar',255,255,empty)

def getContour(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgContour, [cnt], -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)


while True:
    success, img=cap.read()
    if not success:
        break

    imgHVS=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_Min=cv2.getTrackbarPos("HUE min","Trackbar")
    h_max=cv2.getTrackbarPos("HUE max","Trackbar")
    s_Min=cv2.getTrackbarPos("SAT min","Trackbar")
    s_max=cv2.getTrackbarPos("SAT max","Trackbar")
    v_Min=cv2.getTrackbarPos("VAL min","Trackbar")
    v_max=cv2.getTrackbarPos("VAL max","Trackbar")

    lower=np.array([h_Min,s_Min,v_Min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHVS,lower,upper)  

    getContour(mask, img)
    
    cv2.imshow("image",img)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

