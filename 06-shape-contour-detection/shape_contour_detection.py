import cv2
import numpy as np

frameWidth = 480
frameHeight = 540
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

cv2.namedWindow("track")
cv2.resizeWindow("track", 640, 200)
cv2.createTrackbar("threshold1", "track", 50, 255, empty)
cv2.createTrackbar("threshold2", "track", 150, 255, empty)

def getContour(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgContour, [cnt], -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)

while True:
    success, img = cap.read()
    if not success:
        break

    Threshold1 = cv2.getTrackbarPos("threshold1", "track")
    Threshold2 = cv2.getTrackbarPos("threshold2", "track")

    imgBlur = cv2.GaussianBlur(img, (5, 5), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, Threshold1, Threshold2)
    kernel = np.ones((4, 4), np.uint8)
    imgDail = cv2.dilate(imgCanny, kernel, iterations=1)

    getContour(imgDail, img)

    cv2.imshow("Result2", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
