import cv2

cap = cv2.VideoCapture(0) # Parameter passed is Device index (Camera no.) or name of VideoCapture
# cv2 . namedWindow("Video" , cv2 . WINDOW_NORMAL)

"""
if not cap . isOpened() : # Whether cap is initialized or not
    cap . open()
print "Frame width : " + str(cap . get(3)) # Getting values of Property Identifiers
print "Frame height : " + str(cap . get(4))

cap . set(3 , 800) # Changing values of Property Identifiers
cap . set(4 , 800)
"""
fourcc = cv2.cv.CV_FOURCC(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'XVID') # Sets video codecs
out = cv2.VideoWriter("recorded_video.avi" , fourcc , 20.0 , (640 , 480))

while(cap.isOpened()):
    ret, frame = cap.read() # Reading video frame by frame
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.flip(gray, 1)
        out.write(gray)

        cv2.imshow("Video", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()