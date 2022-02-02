"""Program that uses the public key cryptography system based on the RSA algorithm for the process of encrypting and
decrypting a message passed as a txt file."""
import random
import numpy as np

e = 65537  # Default value of the public key exponent
file_extension = '.txt'

# Import a list of prime numbers from a CSV file
dataset = np.genfromtxt(  
    'primesSet.csv',
    delimiter=',',
    dtype='int')


def rsa_coding_system():
    """Execution of the RSA coding system."""

    # Takes a file as input and displays it
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

            # Create a list of text characters in the file
            m_list = []
            for char in str_file:
                m_list += char

            # Randomly select two prime numbers from the dataset
            p = random.choice(dataset)
            q = random.choice(dataset)
            print(p)
            print(q)
            # Calculate the modulus
            n = p * q

            # Calculate the tozient function
            f = (p - 1) * (q - 1)

            # Determines the exponent d of the private key
            d = 0
            i = 1
            condition = True
            while condition:
                check = (i * e) % f
                if check == 1:
                    d = i
                    break
                i = i + 1

            # View the keys
            print('\nKEYS:')
            print(f'Public key: {n, e}')
            print(f'Private key: {n, d}')

            # Performs the encryption process
            encrypted_text = ''
            c_list = []
            for char in m_list:
                m = ord(char)
                c_list.append((m ** e) % n)
                if char == '\n':
                    encrypted_text += '\n'
                else:
                    encrypted_text += str((m ** e) % n)

            # View the contents of the encrypted file
            print('\nENCRYPTED FILE:')
            print(encrypted_text)


            # Save the encrypted file as encrypted_filename.txt
            encrypted_file = 'encrypted_' + file
            with open(encrypted_file, mode='w') as c_file:
                c_file.write(encrypted_text)

            # Performs the decryption process
            decrypted_text = ''
            for c in c_list:
                decrypted_text += (chr((c ** d) % n))

            # View the contents of the dencrypted file
            print('\nCHECK THE PROCESS:\n(decrypted file)')
            print(decrypted_text)
            break


if __name__ == '__main__':
    rsa_coding_system()
