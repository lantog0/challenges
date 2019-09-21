import sys

from requests import Session
from re import match

def do_math(u, n1, n2, n):
    return u + n1 * n + n2 * (n - 1) * n / 2

if __name__ == '__main__':
    url = 'http://challenge01.root-me.org/programmation/ch1/'
    final_url = 'http://challenge01.root-me.org/programmation/ch1/ep1_v.php'

    s = Session()

    body = s.get(url).text.splitlines()

    ns_exp = r'.*\[ ([\-\d]*).*\[ n \* ([\-\d]*) .*'
    u_exp = r'.*0</sub> = (.*)'
    n_exp = r'.*U<sub>(\d*)</sub.*'

    try:
        n1, n2 = map(int, match(ns_exp, body[0]).groups())
        u = int(match(u_exp, body[1]).groups()[0])
        n = int(match(n_exp, body[2]).groups()[0])
    except AttributeError:
        print 'Regex failed'
        sys.exit(1)

    result = do_math(u, n1, n2, n)

    params = {
        'result': result
    }

    print s.get(final_url, params=params).text
