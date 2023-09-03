import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask + cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('fg maskframe', fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv2.destroyAllWindows()