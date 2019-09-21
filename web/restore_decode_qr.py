from PIL import Image, ImageDraw
from qrtools import QR
from requests import Session
from re import match
from base64 import b64decode

def fix_qr(img):
    black = (0, 0, 0)
    white = (255, 255, 255)
    colors = [black, white, black]
    width = 8

    img_name = 'qr.png'
    draw = ImageDraw.Draw(img)

    start_points = [
        (18, 18),
        (18, 218),
        (218, 18)
    ]

    for col_start, row_start in start_points:
        sizes = [(
            col_start + width * x,
            row_start + width * x,
            col_start + ((width**2) - x * width),
            row_start + ((width**2) - x * width)
        ) for x in xrange(3)]

        for size, color in zip(sizes, colors):
            draw.rectangle(size, fill=color)

    img.save(img_name)

    return img_name

def decode_qr(img_name):
    qr = QR()

    if qr.decode(img_name):
        return qr.data.split(' ')[-1].encode('utf-8')
    else:
        return False

def make_img(body, img_name='img.png'):
    r_exp = r'.*?png;base64,(.*?)".*'

    try:
        img_b64 = match(r_exp, body).groups()[0]
        img_src = b64decode(img_b64)

        with open(img_name, 'w') as f:
            f.write(img_src)

        return img_name

    except:
        print '[-] Failed matching image with regular expression.'
        exit(1)

def go():
    s = Session()
    url = 'http://challenge01.root-me.org/programmation/ch7/'

    resp = s.get(url).text
    qr_broken_name = make_img(resp)

    qr_broken = Image.open(qr_broken_name)
    qr_name = fix_qr(qr_broken)
    qr_decoded = decode_qr(qr_name)

    if qr_decoded:
        data = {
            'metu': qr_decoded
        }
        resp = s.post(url, data=data).text

        r_exp = r'.*Congratz, le flag est (\w*)<.*'

        try:
            flag = match(r_exp, resp).groups()[0]

            return flag
        except:
            pass
    else:
        print '[-] Couldn\'t decode qr'

    return False

if __name__ == '__main__':
    flag = go()

    if flag:
        print '[+] Got flag %s' % (flag)
        with open('flag.txt', 'w') as f:
            f.write(flag + '\n')
