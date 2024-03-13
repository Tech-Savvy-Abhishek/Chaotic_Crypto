import cv2
import numpy as np

from lib.image_encryptor import preprocess_key
from lib.image_processor import convert_bgr_to_3channel, convert_to_1d_BGR


def XOR_array(NBm, NGm, NRm, key):
    Xor_Bm = np.array([NBm[i] ^ key[i] for i in range(len(NBm))])
    Xor_Gm = np.array([NGm[i] ^ key[i] for i in range(len(NBm))])
    Xor_Rm = np.array([NRm[i] ^ key[i] for i in range(len(NBm))])
    return Xor_Bm, Xor_Gm, Xor_Rm


def decrypt_to_XOR(img_path, key):
    channel_array = convert_bgr_to_3channel(img_path)
    shape = channel_array[0].shape
    channel_array = convert_to_1d_BGR(channel_array)

    NBm, NGm, NRm = XOR_array(
        channel_array[0], channel_array[1], channel_array[2], key)

    preproced_key, D = preprocess_key(key)

    return NRm, NGm, NBm, D, shape


def reverse_sort_channel(encrypted_image_1d_channel, D):
    temp = zip(encrypted_image_1d_channel, D)
    temp_sort = sorted(temp, key=lambda x: x[1])  # Sort based on the D
    encrypted_1d_sorted, _ = zip(*temp_sort)
    return list(encrypted_1d_sorted)


def perform_reverse_sort_all_channels(NRm, NGm, NBm, D):
    Rm = reverse_sort_channel(NRm, D)
    Gm = reverse_sort_channel(NGm, D)
    Bm = reverse_sort_channel(NBm, D)
    return Rm, Gm, Bm


def get_original_img(Rm, Gm, Bm, original_shapes):
    R_channel = [np.array(Rm[i*original_shapes[1]: (i+1)*original_shapes[1]])
                 for i in range(original_shapes[0])]
    G_channel = [np.array(Gm[i*original_shapes[1]: (i+1)*original_shapes[1]])
                 for i in range(original_shapes[0])]
    B_channel = [np.array(Bm[i*original_shapes[1]: (i+1)*original_shapes[1]])
                 for i in range(original_shapes[0])]

    original_img = np.dstack((B_channel, G_channel, R_channel))

    return original_img


def image_regenerator_main(img_path, key):
    NRm, NGm, NBm, key, original_shapes = decrypt_to_XOR(img_path, key)
    Rm, Gm, Bm = perform_reverse_sort_all_channels(NRm, NGm, NBm, key)
    original_img = get_original_img(Rm, Gm, Bm, original_shapes)

    return original_img
