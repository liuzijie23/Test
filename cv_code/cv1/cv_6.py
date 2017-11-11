#不能运行！！！

# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture(0)        #笔记本默认是0
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('xx.avi',fourcc,20.0,(640,480))

while (cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
