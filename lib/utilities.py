
def hex_to_binary(hex_string):
    # Convert hex to an integer with base 16, then convert that to a binary string
    target_length = len(hex_string) * 4
    binary_string = bin(int(hex_string, 16))[2:].zfill(target_length)  # [2:] to remove the '0b' prefix
    return binary_string

def binary_to_int(binary_string):
    # Convert binary string to integer with base 2
    return int(binary_string, 2)

def xor_binary_strings(bin_str1, bin_str2):
    # Convert binary strings to integers
    num1 = int(bin_str1, 2)
    num2 = int(bin_str2, 2)
    
    # Perform XOR operation
    xor_result = num1 ^ num2
    
    # Convert the result back to a binary string, removing the '0b' prefix
    xor_result_bin = bin(xor_result)[2:]
    
    # Optionally, ensure the result has the same length as the input strings
    max_length = max(len(bin_str1), len(bin_str2))
    xor_result_bin = xor_result_bin.zfill(max_length)
    
    return xor_result_bin

def string_to_16x8_matrix(s):
   
    # Create a 16x8 matrix from the string
    matrix = [list(s[i:i+8]) for i in range(0, len(s), 8)]
    
    return matrix

def rearrange_matrix_rows(matrix, order):
    # Initialize the new matrix with None to indicate unfilled rows
    new_matrix = [None] * 16


    for i in range (0, len(matrix)):
        position = order[i]

        # Find the next available position in case of collision
        while new_matrix[position] is not None:
            position = (position+ 1)%len(matrix)

        new_matrix[position] = matrix[i]


    return new_matrix

def binary_to_int_list(binary_str):
    
    # Split the binary string into chunks of 8 bits
    chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    # Convert each chunk to an integer
    int_list = [int(chunk, 2) for chunk in chunks]
    
    return int_list


import struct


def float_to_binary64(value):
    packed = struct.pack('>d', value)  # Pack the float into 8 bytes
    [integer_value] = struct.unpack('>Q', packed)  # Unpack as a 64-bit/8-byte integer
    return format(integer_value, '064b')  # Format the integer as 64-bit binary


def binary64_to_float(binary_str):
    
    # Convert the binary string to a 64-bit integer
    integer_value = int(binary_str, 2)
    
    # Pack the integer into 8 bytes, then unpack as a double precision float
    packed = struct.pack('>Q', integer_value)
    [float_value] = struct.unpack('>d', packed)
    
    return float_value

def binary_str_to_integers(binary_str):
    # Initialize an empty list to store the resulting integers
    integers = []
    
    # Process each 8-bit chunk of the binary string
    for i in range(0, len(binary_str), 8):

        byte = binary_str[i:i+8]
        if len(byte) == 8:
            # Convert the binary string chunk to an integer and add it to the list
            integers.append(int(byte, 2))
    
    return integers