from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

# calculate center of a shape (average of all points)
def centroid(arr):
    length = arr.shape[0]
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return int(round(sum_x / length)), int(round(sum_y / length))


# calculate polar angle of 2 points
def angle(x1, y1, x2, y2):
    return np.degrees(np.arctan((y2-y1)/(x2-x1)))


def distance(x1, y1, x2, y2):
    return np.sqrt(((x2-x1)**2) + ((y2-y1)**2))


def rotate_image(img, rot_angle, center_x, center_y):
    center = (center_x, center_y)
    rot_mat = cv2.getRotationMatrix2D(center, rot_angle, 1.0)
    result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def translate_image(img, hor_shift, vert_shift):
    h, w = img.shape[:2]
    tran_mat = np.float32([[1, 0, hor_shift], [0, 1, vert_shift]])
    result = cv2.warpAffine(img, tran_mat, (w, h))
    return result


def scale_image(img, scale):
    h, w = img.shape[:2]
    result = cv2.resize(img, (int(scale * w), int(scale * h)), interpolation=cv2.INTER_CUBIC)
    center = (int(result.shape[0]/2), int(result.shape[1]/2))
    background = np.zeros((1080, 1920, 3), np.uint8)
    h, w = result.shape[:2]
    if w >= 1920:
        crop_x = int(1920/2)
    else:
        crop_x = int(w/2)
    if h >= 1080:
        crop_y = int(1080/2)
    else:
        crop_y = int(h/2)

    result = result[(center[0] - crop_y):(center[0] + crop_y), (center[1] - crop_x):(center[1] + crop_x)]
    h, w = result.shape[:2]
    background[int(1080/2-h/2):int(1080/2+h/2), int(1920/2-w/2):int(1920/2+w/2)] = result[0:h, 0:w]
    # cv2.imshow("work", result)
    # cv2.waitKey(0)
    return background


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
image = imutils.resize(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
faces = detector(gray, 1)

# loop over the face detections
for (i, face) in enumerate(faces):
    shape = predictor(gray, face)
    shape = face_utils.shape_to_np(shape)  # 68 points held in a np array
    clone = image.copy()
    landmarks = face_utils.FACIAL_LANDMARKS_IDXS
    height, width = image.shape[:2]

    right_eye_centroid = centroid(shape[landmarks["right_eye"][0]:landmarks["right_eye"][1]])
    left_eye_centroid = centroid(shape[landmarks["left_eye"][0]:landmarks["left_eye"][1]])
    nose_centroid = centroid(shape[landmarks["nose"][0]:landmarks["nose"][1]])
    # calculate between the two eyes (negated because of flipped coordinate grid)
    eye_angle = -1 * angle(right_eye_centroid[0], right_eye_centroid[1], left_eye_centroid[0], left_eye_centroid[1])
    eye_distance = distance(right_eye_centroid[0], right_eye_centroid[1], left_eye_centroid[0], left_eye_centroid[1])

    cv2.circle(clone, right_eye_centroid, 1, (0, 0, 255), -1)
    cv2.circle(clone, left_eye_centroid, 1, (0, 0, 255), -1)
    cv2.circle(clone, nose_centroid, 1, (0, 0, 255), -1)
    cv2.line(clone, right_eye_centroid, left_eye_centroid, (255, 0, 0), 1)
    clone = translate_image(clone, width/2 - nose_centroid[0], height/2 - nose_centroid[1])
    clone = rotate_image(clone, -1 * eye_angle, width/2, height/2)

    # image = imutils.resize(clone, width=1920, height=1080)
    clone = scale_image(clone, 200/eye_distance)

    cv2.imshow("Image", clone)
    cv2.waitKey(0)
