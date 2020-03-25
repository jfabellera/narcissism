import argparse
import glob
import os
import pickle
import face_recognition as fr


def get_faces(path, type):
    encoded = {}
    os.chdir(path)
    for file in glob.glob('*.' + type):
        print("encoding " + file + "...")
        face = fr.load_image_file(file)
        encoding = fr.face_encodings(face)
        if len(fr.face_encodings(face)) > 0:
            encoded[file.split(".")[0]] = encoding[0]
        else:
            print("no face found in " + file)
    return encoded


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", action="store", dest="source",
                        help="source directory of images to index", default="", required=True)
    parser.add_argument("-d", "--destination", action="store", dest="destination",
                        help="destination directory for indexed images", default="")
    parser.add_argument("-t", "--type", action="store", dest="type",
                        help="file extension for images to index", choices=['jpg', 'png'], default="jpg")
    parser.add_argument("-G", "--gui", action="store_true", help=argparse.SUPPRESS)
    args = vars(parser.parse_args())

    if not os.path.isdir(args["source"]):
        print("Source directory could not be found.")
        exit()

    if not os.path.isdir(args["source"]):
        print("Destination directory could not be found.")
        exit()

    if not args["destination"]:
        args["destination"] = "."

    encoded_faces = get_faces(args["source"], args["type"])
    pickle.dump(encoded_faces, open(args["destination"] + "\\trained_faces.dat", "wb"))


if __name__ == "__main__":
    main()
