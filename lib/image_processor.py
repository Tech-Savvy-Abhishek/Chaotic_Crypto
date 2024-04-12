from PIL import Image
import numpy as np


def convert_bgr_to_3channel(img_path):
    imgRGB = Image.open(img_path)
    imgRGB = np.array(imgRGB)
    imgB = imgRGB[:, :, 0]
    imgG = imgRGB[:, :, 1]
    imgR = imgRGB[:, :, 2]
    channel_array = [imgB, imgG, imgR]
    return channel_array


def convert_to_1d_BGR(channel_array):
    channel_array = [channel_array[i].flatten()
                     for i in range(len(channel_array))]
    return channel_array


def image_processor_main(img_path):
    channel_array = convert_bgr_to_3channel(img_path)
    shape = channel_array[0].shape
    channel_array = convert_to_1d_BGR(channel_array)
    return channel_array, shape
