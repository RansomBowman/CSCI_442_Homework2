import numpy as np
import cv2
import copy

vidCap = cv2.VideoCapture(0)

ret, frame = vidCap.read()

avgVal = np.float32(frame)

while True:
    ret, frame = vidCap.read()

    blur = cv2.blur(frame, (5,5))

    cv2.accumulateWeighted(blur, avgVal, .1)
    absVal = cv2.convertScaleAbs(avgVal)

    diff = cv2.absdiff(absVal, frame)

    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

    ret,gray = cv2.threshold(gray,30,255,cv2.THRESH_BINARY)
    gray = cv2.blur(gray, (8,8))
    ret,gray = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

    gray = cv2.dilate(gray, None, iterations = 10)
    gray = cv2.erode(gray, None, iterations = 1)
    gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, None)

    cont, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contoured = copy.deepcopy(frame)
    ret,contoured  = cv2.threshold(gray,255,255,cv2.THRESH_BINARY)
    ret,contoured  = cv2.threshold(gray,255,255,cv2.THRESH_BINARY)

    cv2.drawContours(contoured, cont, -1, (255,255,255), 1)

    for cnt in cont: 
        if cv2.contourArea(cnt) < 4000: 
            continue
        (x, y, w, h) = cv2.boundingRect(cnt) 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Contours', contoured)
    cv2.imshow('Image1', frame)
    cv2.imshow('absDiff Result', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vidCap.release()
cv2.destroyAllWindows()
