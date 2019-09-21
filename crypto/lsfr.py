from sage.all import Matrix, IntegetModRing

to_bin = lambda x: bin(x)[2:].zfill(8)

def get_keystream(read_size=16):
    enc = ''
    plain = ''

    with open(plain_file, 'r') as f:
        plain = f.read(read_size)

    with open(enc_file, 'r') as f:
        enc = f.read(read_size)

    lfsr_key = []

    for x, y in zip(enc, plain):
        x = ord(x)
        y = ord(y)

        lfsr_key.append(x ^ y)


    keystream = ''

    for x in lfsr_key:
        keystream += to_bin(x)

    return keystream

if __name__ == '__main__':
    enc_file = 'challenge.png.encrypt'
    plain_file = 'asdf.png'

    keystream = get_keystream()

    print keystream
