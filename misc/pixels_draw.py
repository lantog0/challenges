from PIL import Image, ImageColor

colors = {
    '0': ImageColor.getcolor('white', '1'),
    '1': ImageColor.getcolor('black', '1')
}

pixels = []

with open('pixels.txt', 'r') as f:
    pixels = [x.split('+') for x in f.read().split('\n')]

pixels = pixels[:-1]

rows = len(pixels)
cols = 1

for size in pixels[0]:
    cols += int(size[2:])


img = Image.new('1', (cols, rows))

for r, arr in enumerate(pixels):
    c = 0
    for pix in arr:
        color = colors(pix[0])
        times = int(pix[2:])

        for _ in range(times):
            img.putpixel((c, r), color)
            c += 1

img.save('done.png')
