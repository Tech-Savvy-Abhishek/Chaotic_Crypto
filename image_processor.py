import numpy as np
import cv2 
import matplotlib.pyplot as plt
import random
import scipy.misc

def convert_bgr_to_3channel(img_path):
    imgBGR = cv2.imread(img_path, -1)
    imgB = imgBGR[:,:,0]
    imgG = imgBGR[:,:,1]
    imgR = imgBGR[:,:,2]
    channel_array = [imgB, imgG, imgR]
    return channel_array 

def convert_to_1d_BGR(channel_array):
    channel_array = [channel_array[i].flatten() for i in range(len(channel_array))]
    return channel_array

def image_processor_main(img_path):
    channel_array = convert_bgr_to_3channel(img_path)
    shape = channel_array[0].shape
    channel_array = convert_to_1d_BGR(channel_array)
    return channel_array, shape