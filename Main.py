'''
A simple program demonstrating a blockchain. Based off of a NeuralNine Youtube video
This program gives you 2 inputs, the password itself and the block size.
This gives a little more security since they both affect the hash.
'''

import hashlib

class password_block:
    def __init__(self, previous_hash, password_string):
        self.previous_hash = previous_hash
        self.password_string = password_string

        self.data = password_string + "," + previous_hash
        self.hash = hashlib.sha256(self.data.encode()).hexdigest()

def hash_password():
    password_blocks = [password[i:i+block_length] for i in range(0, len(password), block_length)]

    block_list = []

    block_list.append(password_block("initial", password_blocks[0]))
    for i in range(1, len(password_blocks)):
        block_list.append(password_block(block_list[i - 1].hash, password_blocks[i]))

    print(block_list[-1].hash)

password = input("Please enter the password you wish to hash: ")
block_length = int(input("Please enter the desired length of each password block: "))

hash_password()
