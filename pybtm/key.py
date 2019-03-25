import random
import hashlib

def get_entropy():
    entropy = random.randint(0, 2**128)
    entropy_hexstr = entropy.to_bytes(16, byteorder='big').hex()
    return entropy_hexstr


# get_mnemonic create mnemonic from 128 bits entropy(the entropy_hexstr length is 32)
# return 12 mnemonics
# You can get more test data from: https://gist.github.com/zcc0721/63aeb5143807950f7b7051fadc08cef0
# test data 1:
#   entropy_hexstr: 1db8b283eb4623e749732a341396e0c9
#   mnemonic_str: buffalo sheriff path story giraffe victory chair grab cross original return napkin
# test data 2:
#   entropy_hexstr: 4d33735a9e92f634d22aecbb4044038d
#   mnemonic_str: essay oppose stove diamond control bounce emerge frown robust acquire abstract brick
# test data 3:
#   entropy_hexstr: 089fe9bf0cac76760bc4b131d938669e
#   mnemonic_str: ancient young hurt bone shuffle deposit congress normal crack six boost despair
def get_mnemonic(entropy_hexstr=None):
    if entropy_hexstr is None:
        entropy_hexstr = get_entropy()
    mnemonic_str = ""
    mnemonic_length = 12

    # create a 12 elements mnemonic_list 
    mnemonic_list = []
    for _ in range(mnemonic_length):
        mnemonic_list.append('')

    entropy_bytes = bytes.fromhex(entropy_hexstr[:32])
    checksum = hashlib.sha256(entropy_bytes).hexdigest()[:1]
    new_entropy_str = "0" + entropy_hexstr[:32] + checksum
    new_entropy_bytes = bytes.fromhex(new_entropy_str)
    new_entropy_int = int.from_bytes(new_entropy_bytes, byteorder='big')

    file = open('english_mnemonic.txt', mode='r')
    word_list = file.readlines()
    file.close()

    for i in range(11, -1, -1):
        word_index = new_entropy_int % 2048
        new_entropy_int = new_entropy_int >> 11
        mnemonic_list[i] = word_list[word_index]

    for i in range(12):
        mnemonic_str += mnemonic_list[i][:-1]
        mnemonic_str += " "
    return mnemonic_str[:-1]
