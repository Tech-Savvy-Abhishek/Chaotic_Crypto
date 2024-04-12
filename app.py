from io import BytesIO
from flask import Flask, request, send_file, render_template
from PIL import Image
from lib.final_key import final_key_generator
from lib.image_encryptor import image_encryptor_main
from lib.image_processor import image_processor_main
from lib.image_regenerator import image_regenerator_main

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/encryption')
def encryption():
    return render_template('encryption.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    numbers = request.form.get('numbers')
    n1, n2, n3, n4, n5, n6 = map(int, numbers.split(','))
    file = request.files['file']
    image = Image.open(BytesIO(file.read()))
    image.save('/tmp/sample.png', format='PNG')
    channel_array, shape = image_processor_main('/tmp/sample.png')
    km = final_key_generator(shape[0]*shape[1], n1, n2, n3, n4, n5, n6)
    encrypted_image = image_encryptor_main(channel_array, km, shape)
# Convert data type to 8-bit unsigned integer
    encrypted_image = encrypted_image.astype('uint8')
    encrypted_image = Image.fromarray(encrypted_image)
    encrypted_image.save('/tmp/encrypted.png')

    return send_file('/tmp/encrypted.png', mimetype='image/png', as_attachment=True)


@app.route('/decryption')
def decryption():
    return render_template('decryption.html')


@app.route('/decrypt', methods=['POST'])
def decrypt():
    numbers = request.form.get('numbers')
    n1, n2, n3, n4, n5, n6 = map(int, numbers.split(','))
    file = request.files['file']
    image = Image.open(file.stream)
    image.save('/tmp/sample.png', format='PNG')
    channel_array, shape = image_processor_main('/tmp/sample.png')
    km = final_key_generator(shape[0]*shape[1], n1, n2, n3, n4, n5, n6)
    decrypted_image = image_regenerator_main('/tmp/encrypted.png', km)
# Convert data type to 8-bit unsigned integer
    decrypted_image = decrypted_image.astype('uint8')
    decrypted_image = Image.fromarray(decrypted_image)
    decrypted_image.save('/tmp/decrypted_image.png')

    return send_file('/tmp/decrypted_image.png', mimetype='image/png', as_attachment=True)
