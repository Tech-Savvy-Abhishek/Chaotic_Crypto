
from lib.final_key import final_key_generator
from lib.image_encryptor import image_encryptor_main
from lib.image_processor import image_processor_main
from lib.image_regenerator import image_regenerator_main
import cv2


n1 = 1567214589126514
n2 = 7214589126514469
n3 = 7214589126514969
n4 = 2721458912651469
n5 = 9721458912651469
n6 = 7214589126514569

# encryption



channel_array, shape = image_processor_main('temp/sample.jpg')
km = final_key_generator(shape[0]*shape[1], n1, n2, n3, n4, n5, n6)

encrypted_image = image_encryptor_main(channel_array, km, shape)
cv2.imwrite('temp/encrypted.png', encrypted_image)


# decryption
channel_array, shape = image_processor_main('temp/encrypted.png')
km = final_key_generator(shape[0]*shape[1], n1, n2, n3, n4, n5, n6)
decrpted_image = image_regenerator_main('temp/encrypted.png', km)
cv2.imwrite('temp/decrypted_image.png',decrpted_image)
