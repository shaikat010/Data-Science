from Crypto.Cipher import AES
import random
import os
import struct


key = ''.join(chr(random.randint(0, 1000)) for i in range(16))
print('key', [x for x in key])
# prints
#key ['+', 'Y', '\xd1', '\x9d', '\xa0', '\xb5', '\x02', '\xbf', ';', '\x15', '\xef', '\xd5', '}', '\t', ']', '9']

iv = ''.join([chr(random.randint(0, 1000)) for i in range(16)])

# Assign values
data = 1281
key = 27

# Display values
print('Original Data:', data)
print('Key:', key)

# Encryption
data = data ^ key
print('After Encryption:', data)

# Decryption
data = data ^ key
print('After Decryption:', data)

# image encryption
try:
    # take path of image as a input
    path = input(r'Enter path of Image : ')

    # taking encryption key as input
    key = int(input('Enter Key for encryption of Image : '))

    # print path of image file and encryption key that
    # we are using
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    # open file for reading purpose
    fin = open(path, 'rb')

    # storing image data in variable "image"
    image = fin.read()
    fin.close()

    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)

    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key

    # opening file for writing purpose
    fin = open(path, 'wb')

    # writing encrypted data in image
    fin.write(image)
    fin.close()
    print('Encryption Done...')


except Exception:
    print('Error caught : ', Exception.__name__)

