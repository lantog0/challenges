import string
import operator

from Crypto.Cipher import AES
from struct import unpack

f_name = 'mylogin.cnf'

def divide(msg, div_len=3):
    chunks = {}

    for x in xrange(div_len, len(msg), div_len):
        chunk = msg[x-div_len:x]

        if chunk in chunks:
            chunks[chunk] += 1
        else:
            chunks[chunk] = 1

    return chunks

def get_printables(msg):
    printable = ''
    #printables = string.ascii_letters + string.digits + '{}/^=\"\':|'
    printables = string.printable

    for x in msg:
        if x in printables:
            printable += x

    return printable

def dec(msg):
    key = [0 for x in xrange(16)]
    
    for x, y in enumerate(msg[4:24]):
        key[x % 16] ^= ord(y)

    key = ''.join([chr(x) for x in key])
    msg = remove_str(msg[24:])

    cipher = AES.new(key, AES.MODE_ECB)

    return cipher.decrypt(msg)

def remove_str(msg):
    zeroes = '\x00' * 3
    bad = ['\x10' + zeroes, '\x20' + zeroes]

    for x in bad:
        msg = msg.replace(x, '')

    return msg

if __name__ == '__main__':
    plain = ''

    with open(f_name, 'r') as f:
        plain = f.read()
    
    print dec(plain)
