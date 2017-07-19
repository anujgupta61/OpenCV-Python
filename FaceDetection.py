# Haar-cascade Detection
# This algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. 
# Then we extract features from it.
import cv2
import numpy as np

# OpenCV already contains many pre-trained classifiers for face, eyes, smile etc.
face_cascade = cv2.CascadeClassifier('HaarCascade\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('HaarCascade\haarcascade_eye.xml')

img = cv2.imread('Images\image2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.namedWindow("My Image", cv2.WINDOW_NORMAL)
cv2.imshow("My Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()