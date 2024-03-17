import numpy as np

def preprocess_key(key):
    # Sort the key and generate corresponding indices
   
    D = [i for i in range(len(key))]
    temp = zip(key, D)
    # Sort the key in descending order
    temp_desc = sorted(temp, key=lambda x: x[0])
    # Rearrange the sorted key and indices
    mix = list(zip(*temp_desc))
   
    temp_desc, D = mix[0][::-1], mix[1][::-1]
    return temp_desc, D

# Function to sort a channel according to the indices in D
def sort_channel(image_1d_channel, D):
    N_image_1d_channel_m = []
    
    for i in range(len(D)):
        N_image_1d_channel_m.append(image_1d_channel[D[i]])
    return N_image_1d_channel_m

# Function to sort BGR channels using the key
def sort_bgr(channel_array, key):
    # Preprocess the key to get sorted key and indices
    key_desc, D = preprocess_key(key)
    
    # Sort each channel according to D
    NBm = sort_channel(channel_array[0], D)
    NGm = sort_channel(channel_array[1], D)
    NRm = sort_channel(channel_array[2], D)
    return NBm, NGm, NRm, key_desc

# Function to perform XOR operation on arrays
def XOR_array(NBm, NGm, NRm, key):
    Xor_Bm = np.array([NBm[i] ^ key[i] for i in range(len(NBm))])
    Xor_Gm = np.array([NGm[i] ^ key[i] for i in range(len(NBm))])
    Xor_Rm = np.array([NRm[i] ^ key[i] for i in range(len(NBm))])
    return Xor_Bm, Xor_Gm, Xor_Rm

# Function to reconstruct the encrypted image from XOR'ed channels
def get_encrypted_img(Xor_Bm, Xor_Gm, Xor_Rm, original_shapes):
    # Reshape XOR'ed channels to original shapes
    B_channel = [np.array(Xor_Bm[i*original_shapes[1]: (i+1)*original_shapes[1]]) for i in range(original_shapes[0])]
    G_channel = [np.array(Xor_Gm[i*original_shapes[1]: (i+1)*original_shapes[1]]) for i in range(original_shapes[0])]
    R_channel = [np.array(Xor_Rm[i*original_shapes[1]: (i+1)*original_shapes[1]]) for i in range(original_shapes[0])]
    encrypter_image = np.dstack((B_channel, G_channel, R_channel))
    return encrypter_image

# Main function for image encryption
def image_encryptor_main(channel_array, key, original_shapes):
    # Sort BGR channels using the key
    NBm, NGm, NRm, _ = sort_bgr(channel_array, key)
    # Perform XOR operation on sorted channels
    Xor_Bm, Xor_Gm, Xor_Rm = XOR_array(NBm, NGm, NRm, key)
    # Reconstruct the encrypted image
    encrypter_image = get_encrypted_img(Xor_Bm, Xor_Gm, Xor_Rm, original_shapes)
    return encrypter_image