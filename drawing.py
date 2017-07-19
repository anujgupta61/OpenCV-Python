import cv2
import numpy as np

# Create a black image
# img = np.zeros((512, 512, 3), np.uint8)

img = cv2.imread("Images\image.jpg", 1)
height, width, channels = img.shape

pts = np.array([[105, 105], [134, 130], [341, 167], [190, 112], [120, 340]], np.int32)
pts.reshape((-1, 1, 2))
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.line(img, (0, 0), (width, height), (255, 0, 0), 5) # BGR color mode
cv2.rectangle(img, (width, 0), (width / 2, height / 2), (0, 255, 0), 3)
cv2.circle(img, (width / 2, height / 2), 100, (0, 0, 255), -1) # -1 will fill the shape with color
cv2.ellipse(img, (width / 4, height / 4), (100, 50 ), 0, 0, 360, (0, 0, 255), -1)
cv2.polylines(img, [pts], True, (0, 255, 255)) # Here True gives the closed polygon
cv2.putText(img, "ANUJ GUPTA", (width / 2, height / 2), font, 1, (255, 255, 0), 3)

cv2.namedWindow("Drawing on images", cv2.WINDOW_NORMAL)
cv2.imshow("Drawing on images", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
