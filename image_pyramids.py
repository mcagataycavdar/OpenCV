import cv2
import numpy as np
img = cv2.imread('lena.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr1 = cv2.pyrUp(lr2)

cv2.imshow("Original image", img)
cv2.imshow("pyrDown_1", lr1)
cv2.imshow("pyrDown_2", lr2)
cv2.imshow("pyrUp_1", hr1)
cv2.waitKey(0)
cv2.destroyAllWindows()