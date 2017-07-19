# os - This module will be used to maneuver with image and directory names
# Image - dataset images are in gif format and as of now, OpenCV does not support gif format, we will use Image module from PIL  to read the image in grayscale format
# cv2 - This is the OpenCV module and contains the functions for face detection and recognition
# numpy  - Our images will be stored in numpy arrays
import cv2, os
import numpy as np
import PIL # PIL - Python Imaging Library
from PIL import Image 

faceCascade = cv2.CascadeClassifier('HaarCascade\haarcascade_frontalface_default.xml')

# OpenCV currently provides 3 face recognizers -
# Eigenface Recognizer - createEigenFaceRecognizer()
# Fisherface Recognizer - createFisherFaceRecognizer()
# Local Binary Patterns Histograms Face Recognizer - createLBPHFaceRecognizer()
# We will use Local Binary Patterns Histograms Face Recognizer.
recognizer = cv2.createLBPHFaceRecognizer()

def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    # return the images list and labels list
    return images, labels

# Path to the Yale Dataset
path = 'YALE\Faces' 
# The folder yalefaces is in the same folder as this python script
# Call the get_images_and_labels function and get the face images and the 
# corresponding labels
images, labels = get_images_and_labels(path)
cv2.destroyAllWindows()

# Perform the training
recognizer.train(images, np.array(labels))

# Testing the Face Recognizer
# Append the images with the extension .sad into image_paths
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
# The more the value of confidence variable is, the less the recognizer has confidence in the recognition. 
# A confidence value of 0.0 is a perfect recognition.