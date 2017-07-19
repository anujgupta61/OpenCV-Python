import cv2
import numpy as np
import time
import timeit

img1 = cv2.imread('Images\messi.jpg')

time1 = time.time()
e1 = cv2.getTickCount() # Gives the no. of clock cycles till this function call
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
time2 = time.time()
t = (e2 - e1)/cv2.getTickFrequency() # Gives the number of clock cycles per second
print t # So it will print the execution time of above function
print time2 - time1
print time1
print cv2.useOptimized() # Check if optimization is enabled
time3 = time.time()
res = cv2.medianBlur(img1,49)
time4 = time.time()
print "Optimized: " + str(time4 - time3)
cv2.setUseOptimized(False)
print cv2.useOptimized()
time3 = time.time()
res = cv2.medianBlur(img1,49)
time4 = time.time()
print "Unoptimized: " + str(time4 - time3)