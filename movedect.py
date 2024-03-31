
## Arunesh j

## created 2024   pyhton 3.9.6


import cv2
import imutils

cam=cv2.VideoCapture(0)   #camera oda name and first is 0 second cam is 1

firstFrame=None   #that is first thrium la bck ground athu none

area=500    #size 500

while True:
    _,img=cam.read()
    text = "Normal"

    img = imutils.resize(img,width=1000)  #resize 

    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #color 2 gray scale img

    gaussianImg = cv2.GaussianBlur(grayImg, (21,21),0)  #smooth blur

    if firstFrame is None:
        firstFrame = gaussianImg   #capture the first frame means pic ,screen or image or bckground
        continue

    imgDiff=cv2.absdiff(firstFrame,gaussianImg)  #absolute difference 

    threshImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]

    threshImg = cv2.dilate(threshImg,None,iterations=2)

    cnts = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:   #full area
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text ="Moving Object Detected"

    print(text)
    cv2.putText(img,text,(10,20),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("cameraFeed",img)

    key=cv2.waitKey(10)
    print(key)
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
