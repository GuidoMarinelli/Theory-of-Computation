# cryptography.py
"""Program that uses the public key cryptography system based on the RSA algorithm for the process of encrypting and
decrypting a message passed as a txt file."""
import random
import numpy as np

e = 65537  # default value of the public key exponent
file_extension = '.txt'

dataset = np.genfromtxt(  # import a list of prime numbers from a CSV file
    'primesSet.csv',
    delimiter=',',
    dtype='int')


def rsa_coding_system():
    """Execution of the RSA coding system."""

    # takes a file as input and displays it
    while True:
        try:
            file_name = input('Enter the name of file to be encoded: ')
            file = file_name + file_extension
            with open(file, mode='r') as files:
                str_file = ''
                for record in files:
                    str_file += record
        except FileNotFoundError:
            print('No such files in the directory.\n ')
        else:
            print('\nTEXT PRESENT IN THE FILE:')
            print(str_file)

            # create a list of text characters in the file
            m_list = []
            for char in str_file:
                m_list += char

            # randomly select two prime numbers from the dataset
            p = random.choice(dataset)
            q = random.choice(dataset)

            #  calculate the modulus
            n = p * q

            # calculate the tozient function
            f = (p - 1) * (q - 1)

            # determines the exponent d of the private key
            d = 0
            i = 1
            condition = True
            while condition:
                check = (i * e) % f
                if check == 1:
                    d = i
                    break
                i = i + 1

            # view the keys
            print('\nKEYS:')
            print(f'Public key: {n, e}')
            print(f'Private key: {n, d}')

            # performs the encryption process
            encrypted_text = ''
            c_list = []
            for char in m_list:
                m = ord(char)
                c_list.append((m ** e) % n)
                if char == '\n':
                    encrypted_text += '\n'
                else:
                    encrypted_text += str((m ** e) % n)

            # view the contents of the encrypted file
            print('\nENCRYPTED FILE:')
            print(encrypted_text)

            # save the encrypted file as encrypted_filename.txt
            encrypted_file = 'encrypted_' + file
            with open(encrypted_file, mode='w') as c_file:
                c_file.write(encrypted_text)

            # performs the decryption process
            decrypted_text = ''
            for c in c_list:
                decrypted_text += (chr((c ** d) % n))

            # view the contents of the dencrypted file
            print('\nCHECK THE PROCESS:\n(decrypted file)')
            print(decrypted_text)
            break


if __name__ == '__main__':
    rsa_coding_system()
