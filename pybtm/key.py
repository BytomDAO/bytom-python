import random

def get_entropy():
    entropy = random.randint(0, 2**128)
    entropy_hexstr = entropy.to_bytes(16, byteorder='big').hex()
    return entropy_hexstr