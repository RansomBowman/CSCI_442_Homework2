import numpy as np
import cv2
#----------------------------
def placeHolder(blank): #not sure if necessary
    pass
        
def getHSV(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_arr = hsv[y,x]
        print("HSV:", hsv_arr)

def erosion(val):
    pass

def dilation(val):
    pass

#----------------------------Part One-----------------

vidCap = cv2.VideoCapture(0)

cv2.namedWindow('Sliders', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Sliders', 550, 300)

cv2.createTrackbar("0H - 180H", 'Sliders', 0, 180, placeHolder)
cv2.createTrackbar("MaxH - 180H", 'Sliders', 180, 180, placeHolder)
cv2.createTrackbar("0S - 255S", 'Sliders', 0, 255, placeHolder)
cv2.createTrackbar("MaxS - 255S", 'Sliders', 255, 255, placeHolder)
cv2.createTrackbar("0V - 255V", 'Sliders', 0, 255, placeHolder)
cv2.createTrackbar("MaxV - 255V", 'Sliders', 255, 255, placeHolder)

while True:
    ret, frame = vidCap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    minH = cv2.getTrackbarPos('0H - 180H', 'Sliders')
    maxH = cv2.getTrackbarPos('MaxH - 180H', 'Sliders')
    minS = cv2.getTrackbarPos('0S - 255S', 'Sliders')
    maxS = cv2.getTrackbarPos('MaxS - 255S', 'Sliders')
    minV = cv2.getTrackbarPos('0V - 255V', 'Sliders')
    maxV = cv2.getTrackbarPos('MaxV - 255V', 'Sliders')

    low = np.array([minH, minS, minV])
    high = np.array([maxH, maxS, maxV])

    mask = cv2.inRange(hsv, low, high)
    hsv_filter = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    hsv_filter = cv2.dilate(hsv_filter, None, iterations = 10)
    hsv_filter = cv2.erode(hsv_filter, None, iterations = 10)

    cv2.imshow('frame', hsv)
    cv2.setMouseCallback('frame', getHSV)

    hsv_ind_frames = np.concatenate((hsv_filter, frame), axis = 1)
    cv2.imshow('H, S, and V Frames', cv2.resize(hsv_ind_frames, None, fx=.7, fy=.7))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vidCap.release()
cv2.destroyAllWindows()


