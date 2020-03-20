import os, glob, datetime, operator
import argparse
from shutil import copyfile
from PIL import Image


# get date taken from an image and convert string to be a valid date string
def get_date_taken(path):
    date_taken = list(Image.open(path)._getexif()[36867])
    date_taken[4] = '-'
    date_taken[7] = '-'
    date_taken[10] = '-'
    return "".join(date_taken)


def main():
    diff_dir = True
    file_dict = {}
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", action="store", dest="source",
                        help="source directory of images to index", default="")
    parser.add_argument("-d", "--destination", action="store", dest="destination",
                        help="destination directory for indexed images", default="")
    parser.add_argument("-t", "--type", action="store", dest="type",
                        help="file extension for images to index", choices=['jpg', 'png'], default="jpg")
    parser.add_argument("-G", "--gui", action="store_true", help=argparse.SUPPRESS)
    args = vars(parser.parse_args())

    # check if source and destination directory exists and change working directory
    if os.path.isdir(args["source"]):
        os.chdir(args["source"])
    else:
        print("Source directory could not be found.")
        exit()

    if args["destination"] == args["source"]:
        diff_dir = False

    if not args["gui"] and not args["destination"]:
        choice = input("Destination directory not specified. Rename files in source directory? (y/n) ")
        if choice.lower() == 'y':
            args["destination"] = args["source"]
            diff_dir = False

    if not os.path.isdir(args["destination"]):
        print("Destination directory could not be found.")
        exit()

    files = glob.glob("*." + args["type"])
    total = len(files) * 2
    cnt = 0

    for file in files:
        if not diff_dir:
            old_file = file
            file = old_file[:-4] + "_old.jpg"
            os.rename(old_file, file)
        date = datetime.datetime.fromisoformat(get_date_taken(args["source"] + "\\" + file))
        milliseconds = int(round(date.timestamp() * 1000))
        file_dict[file] = milliseconds
        if args["gui"]:
            cnt += 1
            print((cnt / total) * 100)

    file_dict = sorted(file_dict.items(), key=operator.itemgetter(1))

    i = 0
    for k, v in file_dict:
        if diff_dir:
            copyfile(k, args["destination"] + "\\" + str(i) + ".JPG")
        else:
            os.rename(k, str(i) + ".JPG")
        i += 1
        if args["gui"]:
            cnt += 1
            print((cnt / total) * 100)


if __name__ == '__main__':
    main()
