import cv2
import numpy as np
import math
from keras.models import load_model
import numpy as np

cap = cv2.VideoCapture(0)
counter = []
for i in range(0,7):
    counter.append(0);
model = load_model('CNN2/whole_model.h5')
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
    #cv2.imwrite("/run/media/sourav/Work/Works/Gesture Recog/data/0/counter[0].jpg",thresh1)
    if k == 49:
        cv2.imwrite('./thresh.jpg', thresh1)
        thresh = cv2.imread('./thresh.jpg')
        thresh = cv2.resize(thresh, (150,150))
        thresh = np.expand_dims(thresh, axis=0)
        print(model.predict(thresh, batch_size = 1, verbose = 0))
    elif k == 27:
        break
