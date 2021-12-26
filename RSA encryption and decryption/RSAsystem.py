# RSAsystem.py
"""Program that uses the public key encryption system based on the RSA algorithm for the process of encrypting
and decrypting a message."""
import random
import numpy as np

dataset = np.genfromtxt(  # import a list of prime numbers from a CSV file
    'primesSet.csv',
    delimiter=',',
    dtype='int')


# execution of the RSA coding system
def rsa_coding_system():
    message_to_encoded = input('Enter the message to be encoded: ')
    p = random.choice(dataset)
    q = random.choice(dataset)
    n, e = do_public_key(p, q)
    n, d = do_private_key(p, q, e)
    encrypted_message, encrypted_message_list = encryption_process(n, e, message_to_encoded)
    print(f'Public key: {n, e}')
    print(f'Private key: {n, d}')
    print('\nEncrypted message:')
    print(encrypted_message_list)
    print(encrypted_message)
    decrypted_message = decryption_process(n, d, encrypted_message_list)
    print('\nDecrypted message:')
    print(decrypted_message)


# compute the public key
def do_public_key(p, q):
    e_list = []
    n = p * q
    tozient_function = (p - 1) * (q - 1)
    i = 2
    while i < tozient_function:  # determines and chooses the exponent e of the public key
        check = tozient_function % i
        if check == 1:
            e_list.append(i)
        i = i + 1
    e = random.choice(e_list)
    return n, e


# compute the private key
def do_private_key(p, q, e):
    d = 0
    n = p * q
    tozient_function = (p - 1) * (q - 1)
    i = 1
    condition = True
    while condition:  # determines the exponent d of the private key
        check = (i * e) % tozient_function
        if check == 1:
            d = i
            break
        i = i + 1
    return n, d


# performs the encryption process
def encryption_process(n, e, message_to_encoded):
    encrypted_message = ''
    encrypted_message_list = []
    for char in message_to_encoded:
        char = ord(char)
        encrypted_message += str((char ** e) % n)
        encrypted_message_list.append((char ** e) % n)
    return encrypted_message, encrypted_message_list


# performs the decryption process
def decryption_process(n, d, encrypted_message):
    decrypted_message = ''
    for value in encrypted_message:
        decrypted_message += (chr((value ** d) % n))
    return decrypted_message


rsa_coding_system()
