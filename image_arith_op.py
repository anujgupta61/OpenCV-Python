import cv2
import numpy as np

cv2.namedWindow("Addition of Images", cv2.WINDOW_NORMAL)

# Addition of two images
# Using opencv
img1 = cv2.imread("Images\image.jpg", 1)
img1 = cv2.resize(img1, (450, 280))
img2 = cv2.imread("Images\messi.jpg", 1)
img3 = cv2.add(img1, img2) # Gives better result ; Image more visible

# Using numpy
img4 = img1 + img2

# Image blending
# Making an Image slider
x = 0.00
while(x != 1.00):
    img5 = cv2.addWeighted(img1, x, img2, 1 - x, 0)
    x = x + 0.01
    cv2.imshow("Addition of Images", img5)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()