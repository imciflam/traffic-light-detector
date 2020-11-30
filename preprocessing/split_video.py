
#python split_video.py --pathIn /Users/user/downloads/ds1/3_20191113-164801_4003p0.mp4
import sys
import argparse
import os
import cv2 

def extractImages(pathIn):
    videos_path = "/Users/user/downloads/ds1"
    video_list = (os.listdir("/Users/user/downloads/ds1"))
    for video in video_list:
        count = 0
        current_video_path = videos_path+'/'+ video
        vidcap = cv2.VideoCapture(current_video_path)
        success,image = vidcap.read()
        success = True
        while (success and count < 50):
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # sampling rate 
            success,image = vidcap.read()
            print('Read a new frame: %d'% count)

            cv2.imwrite(os.path.abspath(os.getcwd())+"/image_folder/" + "/frame-"+str(count)+video+".jpg", image)
            count += 1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    args = a.parse_args()
    extractImages(args.pathIn)
