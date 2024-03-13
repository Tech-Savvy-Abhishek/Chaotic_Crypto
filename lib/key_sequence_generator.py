from hashlib import sha256

from lib.conversion_utils import henon_to_binary, kaplan_yorke_to_binary, tinkerbell_to_integer
from lib.henon_map import generate_henon_map
from lib.kaplan_yorke_map import generate_keplan_yorke_map
from lib.tinkerbell_map import generate_tinkerbell_map
from lib.utilities import binary_to_int, binary_to_int_list, hex_to_binary, rearrange_matrix_rows, string_to_16x8_matrix, xor_binary_strings


def generate_key_sequence(key_float):

    key_int = []

    # generate 6 integers

    for i in range(0, 6):
        key_int.append((key_float[i]) % 256)

    # sha 256
    key_sha = []
    for i in range(0, 6):
        key_sha.append(sha256(str(key_int[i]).encode('utf-8')).hexdigest())

    # H to B
    key_bin = []
    for i in range(0, 6):
        key_bin.append(hex_to_binary(key_sha[i]))

    # B to N

    input = []
    for i in range(0, 6):
        input.append((binary_to_int(key_bin[i][:50]))*(10**-16))

    # Henon
    henon_output = generate_henon_map(input[0], input[1], 16)
    str1 = henon_to_binary(henon_output[0], henon_output[1])
    # kaplan yorke
    ky_output = generate_keplan_yorke_map(input[2], input[3], 16)
    str2 = kaplan_yorke_to_binary(ky_output[0], ky_output[1])

    # xor

    str3 = xor_binary_strings(str1, str2)

    # reshape to matrix

    str3_mat = string_to_16x8_matrix(str3)

    # tinkerbell
    tb_output = generate_tinkerbell_map(input[4], input[5], 16)
    Tb = tinkerbell_to_integer(tb_output[0], tb_output[1])
    # permute

    final_mat = rearrange_matrix_rows(str3_mat, Tb)
    # revert matrix reshape
    km = ""
    for i in range(0, len(final_mat)):
        for j in range(0, len(final_mat[0])):
            km += (final_mat[i][j])
    final_km = binary_to_int_list(km)

    return str3, final_km
