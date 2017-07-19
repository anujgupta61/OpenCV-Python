# Not solved

import cv2, os
import numpy as np
import PIL # PIL - Python Imaging Library
from PIL import Image 

faceCascade = cv2.CascadeClassifier('HaarCascade\haarcascade_frontalface_default.xml')

recognizer = cv2.createLBPHFaceRecognizer()

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    images = []
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        print "Image path: ", image_path
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        cv2.imshow("Image: ", image)
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        i = 1
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            print "inside"
            images.append(image[y: y + h, x: x + w])
            labels.append(i)
            i = i + 1
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    # return the images list
    return images, labels

path = 'Images\Waldo\Train' 
images, labels = get_images_and_labels(path)
cv2.destroyAllWindows()

# Perform the training
print images
print labels
recognizer.train(images, np.array(labels))

# Testing the Face Recognizer
faces = faceCascade.detectMultiScale(r'Images\Waldo\waldo1')
i = 1
for (x, y, w, h) in faces:
    print i
    i = i + 1

"""
image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]
for image_path in image_paths:
	predict_image_pil = Image.open(image_path).convert('L')
	predict_image = np.array(predict_image_pil, 'uint8')
	faces = faceCascade.detectMultiScale(predict_image)
	for (x, y, w, h) in faces:
	    nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
	    nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
	    if nbr_actual == nbr_predicted:
	        print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
	    else:
	        print "{} is Incorrectly Recognized as {}".format(nbr_actual, nbr_predicted)
	    cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
	    cv2.waitKey(1000)
"""