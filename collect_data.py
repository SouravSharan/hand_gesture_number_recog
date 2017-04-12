import cv2
import numpy as np
import math
cap = cv2.VideoCapture(0)
counter = [0,0,0,0,0,0] # change values if you want to add more images or this will overwrite the existing data

while(cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img,(0,0),(200,200),(0,255,0),0)
    crop_img = img[0:200, 0:200]
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('img', img)
    cv2.imshow('Thresholded', thresh1)

    k = cv2.waitKey(10)
    
    if k == 48: #0
        cv2.imwrite("./data/0/"+ str(counter[0]) + ".jpg",thresh1)
        counter[0] = counter[0] + 1
    elif k == 49:
        cv2.imwrite("./data/1/"+str(counter[1])+".jpg",thresh1)
        counter[1] = counter[1] + 1
    elif k == 50:
        cv2.imwrite("./data/2/"+str(counter[2])+".jpg",thresh1)
        counter[2] = counter[2] + 1
    elif k == 51:
        cv2.imwrite("./data/3/"+str(counter[3])+".jpg",thresh1)
        counter[3] = counter[3] + 1
    elif k == 52:
        cv2.imwrite("./data/4/"+str(counter[4])+".jpg",thresh1)
        counter[4] = counter[4] + 1
    elif k == 53:
        cv2.imwrite("./data/5/"+str(counter[5])+".jpg",thresh1)
        counter[5] = counter[5] + 1
    elif k == 54:
        cv2.imwrite("./data/6/"+str(counter[6])+".jpg",thresh1)
        counter[6] = counter[6] + 1
    elif k == 27:
        break
