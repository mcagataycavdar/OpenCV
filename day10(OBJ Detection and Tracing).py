import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0);
cv2.namedWindow("Tracing")
cv2.createTrackbar("LH", "Tracing", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracing", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracing", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracing", 255, 255, nothing)
cv2.createTrackbar("US", "Tracing", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracing", 255, 255, nothing)

while True:
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracing")
    l_s = cv2.getTrackbarPos("LS", "Tracing")
    l_v = cv2.getTrackbarPos("LV", "Tracing")

    u_h = cv2.getTrackbarPos("UH", "Tracing")
    u_s = cv2.getTrackbarPos("US", "Tracing")
    u_v = cv2.getTrackbarPos("UV", "Tracing")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key =cv2.waitKey(1)
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()