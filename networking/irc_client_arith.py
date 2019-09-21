from pwn import *
from math import sqrt

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
    msg = 'PRIVMSG Candy : !ep1'
    irc.sendline(msg)
    irc.recvuntil(':Candy!Candy@root-me.org PRIVMSG lantog :')
    n1, n2 = [int(x) for x in irc.recvuntil('\n').strip().split('/')]

    return n1, n2

def do_challenge(n1, n2):
    res = round(sqrt(n1) * n2, 2)
    msg = 'PRIVMSG Candy : !ep1 -rep %s' % str(res)
    print msg
    irc.sendline(msg)
    irc.interactive()


if __name__ == '__main__':
    host = 'irc.root-me.org'
    port = 6667
    irc = remote(host, port)

    register()
    irc.recvuntil('MODE lantog +x')
    n1, n2 = get_challenge()
    do_challenge(n1, n2)
