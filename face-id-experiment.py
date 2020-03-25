import argparse
import glob
import os
import pickle

import cv2
import face_recognition as fr
import imutils
import numpy as np
from dlib import rectangle


def encode_unknown(img):
    f = fr.load_image_file(img)
    return fr.face_encodings(f)[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--trained_faces", required=True, help="path to trained_face.dat")
    parser.add_argument("-i", "--image", required=True, help="path to input image")
    args = vars(parser.parse_args())

    trained = pickle.load(open(args["trained_faces"], "rb"))
    trained_name = list(trained.keys())
    trained_enc = list(trained.values())

    os.chdir("test-indexed")
    for file in glob.glob("*.JPG"):

        image = cv2.imread(file, 1)
        image = imutils.resize(image, 1080)

        face_locations = fr.face_locations(image)
        unknown_face_encodings = fr.face_encodings(image, face_locations)

        face_names = []
        for face in unknown_face_encodings:
            matches = fr.compare_faces(trained_enc, face, tolerance=0.45)
            name = "unknown"

            face_distances = fr.face_distance(trained_enc, face)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                # name = trained_name[best_match_index]
                name = 'me'
            face_names.append(name)

        if 'me' in face_names:
            face_temp = face_locations[face_names.index('me')]
        elif len(face_locations) > 0:
            face_temp = face_locations[0]
        else:
            continue
        face = rectangle(face_temp[3], face_temp[0], face_temp[1], face_temp[2])

        cv2.rectangle(image, (face.left()-20, face.top()-20), (face.right()+20, face.bottom()+20), (255, 0, 0), 2)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
    print("done")


if __name__ == "__main__":
    main()
