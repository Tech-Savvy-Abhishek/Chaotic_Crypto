# function to recieve an image, processs into matrix and split into respective channels of rgb
import cv2
import numpy as np
# Function to convert an RGB image to three separate channels
def convert_rgb_to_3channel(img_path):
    # Read the image in BGR format
    imgBGR = cv2.imread(img_path, -1)
    
    # Convert BGR to RGB
    imgRGB = imgBGR[...,::-1]
    
    # Separate the RGB channels
    imgR = imgRGB[:, :, 0]
    imgG = imgRGB[:, :, 1]
    imgB = imgRGB[:, :, 2]
    
    # Store the channels in an array
    channel_array = [imgR, imgG, imgB]
    
    return channel_array

# Function to convert each channel array to a 1D array
def convert_to_1d_RGB(channel_array):
    # Flatten each channel array to convert it to 1D
    channel_array = [channel_array[i].flatten() for i in range(len(channel_array))]
    
    return channel_array

# Main function for image processing
def image_processor(path):
    # Convert the RGB image to three separate channels
    channel_array = convert_rgb_to_3channel(path)
    
    # Convert each channel to a 1D array
    channel_array = convert_to_1d_RGB(channel_array)
    
    return channel_array
