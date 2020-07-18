from cv2 import *
from emotiondetect import *

cam=VideoCapture(0)

while True:
    res,img=cam.read()
    if res:
        imshow('Camera Feed',img)
        t=waitKey(1)
        if(t==ord('s')):
            print ('Image Catpured')
            imwrite('feed.jpg',img)
            main()
