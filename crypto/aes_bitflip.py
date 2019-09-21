from base64 import b64encode, b64decode
from pwn import *

def encode(s):
    b_start = 80
    msg_start =  [x for x in b64decode(s)]
    act_msg = '\xcd\x1c\xba\xfe^\xcb\x13\xb56\x02\xbc\xfe9\xb5D\x90'
    target_msg = [ord(x) for x in ';is_member=true]']

    for x in xrange(16):
        right = ord(msg_start[b_start+x]) ^ ord(act_msg[x])
        msg_start[b_start+x] = chr(target_msg[x] ^ right)

    return b64encode(''.join(msg_start))

def create(name='', fill='a', mail='test'):
    length = 33
    full_name = name + fill * (length - len(name))

    r.line()
    r.sendline('1')
    r.recvuntil(':')
    r.sendline(full_name)
    r.recvuntil(':')
    r.sendline(mail)
    r.recvuntil('Your token is : ')
    token = r.recvline().strip().replace('\'', '')
    r.line()

    return token

host = 'challenge01.root-me.org'
port = 51035

if __name__ == '__main__':
    r = remote(host, port)
    r.line = lambda: r.recvuntil('>>')
    token = create()
    token = b64encode(b64decode(token) + '\x61' * 16)
    print token
    print encode(token)
    break
