import cv2
import numpy as np

img = cv2.imread('/Resources/ballon.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(imgGray, 127, 255)
_, contours, _ = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255,0,0), 2)
cv2.imshow('Result', img)
cv2.waitKey(0)