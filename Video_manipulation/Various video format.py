import numpy as np
import cv2

vid=cv2.VideoCapture(0)

if not vid.isOpened:
    print("We were unable to capture the video.")
    exit()
while True:
    ret,frame=vid.read()
    frame2=frame.copy()
    if not ret:
        print("unable to recive the frame.")
        break
    lowerBlue=np.array([110,50,50])
    upperBlue=np.array([130,255,255])
    frame2=cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV_FULL)
    frame3=cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV_FULL)
    cv2.inRange(frame2,lowerBlue,upperBlue)
    res=cv2.bitwise_and(frame2,frame)
    ##concate=cv2.hconcat([frame,frame2])
    ##cv2.imshow("blue objects",concate)
    cv2.imshow("Original",frame)
    cv2.imshow("Blue",frame2)
    cv2.imshow("Other",frame3)
    if cv2.waitKey(1)==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()