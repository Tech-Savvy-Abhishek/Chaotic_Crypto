
from lib.final_key import final_key_generator
from lib.image_encryptor import image_encryptor_main
from lib.image_processor import image_processor_main
from lib.image_regenerator import image_regenerator_main


n1 = 1567214589126514
n2 = 7214589126514469
n3 = 7214589126514969
n4 = 2721458912651469
n5 = 9721458912651469
n6 = 7214589126514569

# encryption
channel_array, shape = image_processor_main('temp/original.png')
km = final_key_generator(len(channel_array), n1, n2, n3, n4, n5, n6)
encrypted_image = image_encryptor_main(channel_array, km, shape)
encrypted_image.save('temp/encrypted.png', format='PNG')


# decryption
channel_array, shape = image_processor_main('temp/encrypted.png')
km = final_key_generator(len(channel_array), n1, n2, n3, n4, n5, n6)
decrpted_image = image_regenerator_main('temp/processed_image.png', km)
decrpted_image.save('temp/decrpted_image.png', format='PNG')
