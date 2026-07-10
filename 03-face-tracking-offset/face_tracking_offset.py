import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

frameCenterX = frameWidth // 2
frameCenterY = frameHeight // 2

smoothPan = 90
smoothTilt = 90
alpha = 0.3

while True:
    success, img = cap.read()
    if not success:
        break

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4, minSize=(30, 30))

    if len(faces) > 0:
        faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
        (x, y, w, h) = faces[0]

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = imgGray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roi_gray, 1.05, 4, minSize=(20, 20), maxSize=(80, 80))

        faceCenterX = x + w // 2
        faceCenterY = y + h // 2

        cv2.circle(img, (faceCenterX, faceCenterY), 5, (0, 0, 255), -1)

        offsetX = faceCenterX - frameCenterX
        offsetY = faceCenterY - frameCenterY

        panAngle = np.interp(offsetX, [-frameCenterX, frameCenterX], [180, 0])
        tiltAngle = np.interp(offsetY, [-frameCenterY, frameCenterY], [180, 0])

        panAngle = int(panAngle)
        tiltAngle = int(tiltAngle)

        smoothPan = alpha * panAngle + (1 - alpha) * smoothPan
        smoothTilt = alpha * tiltAngle + (1 - alpha) * smoothTilt

        print("smoothed:", int(smoothPan), int(smoothTilt))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
