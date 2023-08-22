import cv2
import numpy as np

img = np.zeros((250, 500, 3), np.uint8)
img = cv2.rectangle(img, (250, 0), (500, 250), (255, 255, 255), -1)

cv2.imwrite('image_2.png', img)
cv2.imshow('blackAndwhite', img)

cv2.waitKey()
cv2.destroyAllWindows()