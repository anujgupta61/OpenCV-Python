import cv2
import numpy as np

img = cv2 . imread("image.jpg" , 1)

# Using opencv
px = img[100 , 100] # Getting pixel value at particular point
print px
img[100 , 100] = [255 , 0 , 0] # Changing pixel value

# Using numpy
print img . item(100 , 100 , 0) # Getting pixel value
img . itemset((100 , 100 , 0) , 100) # Changing pixel value
print img . item(100 , 100 , 0)

print img . shape # No. of rows , columns and channels (If image is colored)
print img . size # Total no. of pixels
print img . dtype # Image datatype
# ROI (Not working)
glass = img[563 : 808 , 916 : 894]
img[463 : 708 , 816 : 794] = glass
# Splitting and merging channels
# Using opencv
b , g , r = cv2 . split(img)
img = cv2 . merge((b , g , r))
# Using numpy
b = img[: , : , 0]
img[: , : , 2] = 0 # Setting all red pixels to 0
# Making border for images
BLUE = [255 , 0 , 0]
img_dest = cv2 . copyMakeBorder(img , 50 , 50 , 50 , 50 , cv2 . BORDER_CONSTANT , value = BLUE)

cv2 . namedWindow("Image" , cv2 . WINDOW_NORMAL)
cv2 . imshow("Image" , img_dest)
cv2 . waitKey(0)
cv2 . destroyAllWindows()
