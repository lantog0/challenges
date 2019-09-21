from base64 import b64decode
from requests import Session
from re import match
from sys import exit
from subprocess import check_output

def get_img_value(filename):
    return check_output(['gocr', filename]).strip().replace('_', '')

def make_img(body, img_name='img.png'):
    r_exp = r'.*?png;base64,(.*?)".*'

    try:
        img_b64 = match(r_exp, body).groups()[0]
        img_src = b64decode(img_b64)

        with open(img_name, 'w') as f:
            f.write(img_src)

        return img_name

    except:
        print 'Failed matching the string'
        exit(1)
        
def debug():
    s.proxies.update({
        'http': 'http://127.0.0.1:8080/'
    })

if __name__ == '__main__':
    url = 'http://challenge01.root-me.org/programmation/ch8/'
    s = Session()
    body = s.get(url).text

    img_name = make_img(body)
    value = get_img_value(img_name)

    data = {
        'cametu': value
    }

    print s.post(url, data=data).text
