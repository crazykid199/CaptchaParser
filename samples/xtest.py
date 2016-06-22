from PIL import Image
import sys

im = Image.open(sys.argv[1])
im2 = im.copy()
pix2 = im2.load()
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

full = []
for i, row in enumerate(pixels):
    r = []
    for k, pix in enumerate(row):
        r.append(pix)
    full.append(r)

print full
