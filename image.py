import cv2

img = cv2.imread("Images\image.jpg", -1) # 1 for color image , 0 for grayscale image , -1 for as it is image including alpha channel
# print img

cv2.namedWindow("My Image", cv2.WINDOW_NORMAL) # Create an empty resizeable window
cv2.imshow("My Image", img)

k = cv2.waitKey(0) & 0xFF # waits for time interval given in parameter (in milli-seconds)
						  # checks whether any keyboard activity is happened
						  # accordingly closes the window
						  # 0 means wait for indefinite time
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'): # ord() function returns the unicode of a character; inverse of chr() function
    cv2.imwrite("Images\image1.jpg", img)
    cv2.destroyAllWindows()