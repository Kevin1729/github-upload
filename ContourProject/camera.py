import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()



while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Convert to binary image
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 140, 255, 0)
    # Find contours
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Display frame with all contours
    cv.imshow("Display Window",cv.drawContours(frame, contours, -1, (255,0,255), 2))

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
