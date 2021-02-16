##import cv2 as cv
##import numpy as np
##
##src = cv.imread("japaneseflowers.jpg", 1)
##if src is None:
##    print("missing image")
##
##cv.imshow("windoMy", src)
### else:
###     gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
###     final = cv.Canny(gray, 75,200)
###     cv.imshow("Original", gray)
###     cv.imshow("adaptive", final)

##import cv2 as cv
##import numpy as np
##
##src = cv.imread("japaneseflowers.jpg", 1)
##if src is None:
##    print("missing image")
##else:
##    gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
##    final = cv.Canny(gray, 75,200)
##    cv.imshow("Original", gray)
##    cv.imshow("adaptive", final)   

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
