
from lib.key_sequence_generator import generate_key_sequence
from lib.utilities import binary_str_to_integers


def final_key_generator(size, n1, n2, n3, n4, n5, n6):
  n = int(size / 16)
  if (size % 16):
    n += 1

  final_key = []
  key = [n1, n2, n3, n4, n5, n6]
  for i in range(n):
    temp_key = generate_key_sequence(key)
    final_key += temp_key
  
    new_key = []
    for j in range(len(key)):
      new_key.append(
          abs((key[j] * key[(j + 1) % len(key)]) + key[(j + 2) % len(key)]) % (10**16))
    key = new_key
    
  final_key = final_key[:size]
  return final_key
