
from lib.key_sequence_generator import generate_key_sequence
from lib.utilities import binary_str_to_integers


def final_key_generator(size, n1, n2, n3, n4, n5, n6):
  n = int(size / 128)
  if (size % 128):
    n += 1
  final_key = ""
  key = [n1, n2, n3, n4, n5, n6]
  for i in range(n):
    str1, str2, temp_key = generate_key_sequence(
        key[0], key[1], key[2], key[3], key[4], key[5])
    final_key += temp_key
    new_key = []
    for i in range(len(key)):
      new_key.append(
          abs((key[i] * key[(i + 1) % len(key)]) + key[(i + 2) % len(key)]) % (10**16))
    key = new_key

  final_key = final_key[:size]
  int_key = binary_str_to_integers(final_key)
  return int_key
