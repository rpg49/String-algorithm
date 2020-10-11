import cv2
import numpy as np 
import imutils

#image read
# print("Package imported")
# img = cv2.imread("resources/rp.jpg")
# half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
# reimg = cv2.resize(img,(300,200))
# imagegray = cv2.cvtColor(reimg,cv2.COLOR_BGR2GRAY)
# imagecanny = cv2.Canny(reimg,150,200)
# kernel = np.ones((5,5),np.uint8)
# imagedialation = cv2.dilate(imagecanny,kernel,iterations = 5)
# cv2.imshow("output",reimg)
# cv2.imshow("Grayimage",imagegray)
# cv2.imshow("cannyimage",imagecanny)
# cv2.imshow("imagedialation",imagedialation)
# cv2.waitKey(0)    

#Read video 
# cap = cv2.VideoCapture("resources/songlaunch.mp4")
# while True :
#     success , img = cap.read()
#     cv2.imshow("video",img)

#     if cv2.waitKey(1) and 0xFF == ord('q'):
#         break 

#Read webcam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# while True :
#     success , img = cap.read()
#     cv2.imshow("video",img)

#     if cv2.waitKey(1) and 0xFF ==ord('q'):
#         break 
 
 #Shapes and Texts
# img = np.zeros((512,512))
# cv2.imshow("Image",img)
# cv2.waitKey(0)


# Hand recognition with image :

# hand = cv2.imread("resources/hand.jpg",0)
# half = cv2.resize(hand, (0, 0), fx = 0.1, fy = 0.1)
# reimg = cv2.resize(hand,(300,200))
# ret , the = cv2.threshold(reimg,70,255, cv2.THRESH_BINARY)
# _ ,contours = cv2.findContours(the.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
# hull = cv2.convexHull(cnt,returnPoints = False)
# defects = cv2.convexityDefects(cnt,hull)
# final = cv2.drawContours(hand,hull,-1,(255,0,0))
# cv2.imshow('Originals', reimg)
# cv2.imshow('Thresh',the)
# cv2.imshow('Convex hull',final)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
    

# img = cv2.imread("resources/hand.jpg")
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
# contours,hierarchy = cv2.findContours(thresh,2,1)
# cnt = contours[0]
# hull = cv2.convexHull(cnt,returnPoints = False)
# defects = cv2.convexityDefects(cnt,hull)
# # final = cv2.drawContours(img,hull,-1,(255,0,0))

# cv2.imshow('Originals', img)
# cv2.imshow('Thresh',thresh)
# cv2.imshow('Convex hull',img_gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()    

# Text on image

img = np.zeros((512,512,3),np.uint8)
cv2.putText(img,"OPENCV",(200,200),cv2.FONT_HERSHEY_COMPLEX, 2,(0,150,0),1)
