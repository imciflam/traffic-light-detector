
#python split_video.py --pathIn /Users/user/downloads/ds1/3_20191113-164801_4003p0.mp4
import sys
import argparse
import os
import cv2
print(cv2.__version__)

def extractImages(pathIn):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while (success and count < 300):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
        success,image = vidcap.read()
        print('Read a new frame: %d'% count)
        cv2.imwrite(os.path.abspath(os.getcwd())+"/image_folder" + "/frame%d.jpg" % count, image)    # save frame as JPEG file
        count += 1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    args = a.parse_args()
    extractImages(args.pathIn)
