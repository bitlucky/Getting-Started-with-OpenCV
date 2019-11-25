# -*- coding: utf-8 -*-
import cv2
img = cv2.imread("abc.jpg", 1)
img = cv2.line(img , (0,0) , (255,255) ,(147,86,91) , 10 )
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
