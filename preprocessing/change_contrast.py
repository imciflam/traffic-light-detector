import sys
import argparse
import os
import cv2
import numpy as np

def change_contrast(): 
    images_path = os.getcwd() + "/image_folder/"
    #images_list = (os.listdir(images_path)) 
    example_path = images_path+"frame-373_20191113-084800_4003p0.mp4.jpg"
    image = cv2.imread(example_path)
    if image is None:
        print('Could not open or find the image')

    alpha = 1.2 # Simple contrast control
    beta = 0.2    # Simple brightness control
    new_image = np.zeros(image.shape, image.dtype)

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)

    # cv2.imshow('Original Image', image)
    cv2.imshow('New Image', new_image)




if __name__=="__main__": 
    change_contrast()
