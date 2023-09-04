#Modules
import cv2
import time


#Take picture
cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

cam.set(cv2.CAP_PROP_FOURCC, 0x32595559)

cam.set(cv2.CAP_PROP_FPS, 30)

img_counter = 0

# Open test window
cv2.namedWindow('test')

while True:
    ret,frame=cam.read() 
    if not ret:
        time.sleep(5)
        print('failed to grab frame')
        break

    cv2.imshow('test',frame)

    k = cv2.waitKey(1)

#set key bindings
    if k%256 == 27:
        time.sleep(5)
        print('Escape hit, closing the app')
        break
    elif k%256 == 32:
        img_name= 'opencv_frame_{}.png'.format(img_counter)
        cv2.imwrite(img_name,frame)
        print('screenshot taken')
        img_counter+=1