from pwn import *
from base64 import b64decode
from zlib import decompress

def register(nick_name='lantog', password='asdf'):
    reg_user = 'USER %s 0 * :adsf' % (nick_name)
    reg_pass = 'PASS %s' % (password) 
    reg_nick = 'NICK %s' % (nick_name)
    reg_channel = 'JOIN #root-me_challenge'

    irc.sendline(reg_user)
    irc.sendline(reg_pass)
    irc.sendline(reg_nick)
    irc.sendline(reg_channel)

def get_challenge():
    msg = 'PRIVMSG Candy : !ep4'
    irc.sendline(msg)
    irc.recvuntil(':Candy!Candy@root-me.org PRIVMSG lantog :')
    
    return irc.recvline().strip()

def do_challenge(enc_msg):
    try:
        msg = 'PRIVMSG Candy : !ep4 -rep %s' % (decompress(b64decode(enc_msg)))
        irc.sendline(msg)
        flag = irc.recvline()
        print flag
        with open('flag.txt', 'w') as f:
            f.write(flag)
    except:
        print 'Error decoding %s' % enc_msg

if __name__ == '__main__':
    host = 'irc.root-me.org'
    port = 6667
    irc = remote(host, port)

    register()
    irc.recvuntil('MODE lantog +x')
    msg = get_challenge()
    do_challenge(msg)

