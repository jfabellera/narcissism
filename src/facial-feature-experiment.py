from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor")
parser.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(parser.parse_args())

# initialize dlib's face detector (HOG-based) and then create the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# load the input image, resize it, and convert it to grayscale
image = cv2.imread(args["image"])
image = imutils.resize(image, width=1000)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
faces = detector(gray, 1)

# loop over the face detections
for (i, face) in enumerate(faces):
    shape = predictor(gray, face)
    shape = face_utils.shape_to_np(shape)  # 68 points held in a np array

    # loop over the face parts individually
    for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
        # clone the original image so we can draw on it, then
        # display the name of the face part on the image
        clone = image.copy()
        cv2.putText(clone, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # loop over the subset of facial landmarks, drawing the specific face part
        for (x, y) in shape[i:j]:
            cv2.circle(clone, (x, y), 1, (0, 0, 255), -1)

        cv2.imshow("Image", clone)
        cv2.waitKey(0)

    cv2.waitKey(0)
