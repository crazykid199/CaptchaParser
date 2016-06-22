from PIL import Image
import csv


from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("tatkal-output") if isfile(join("tatkal-output", f))]
for file in onlyfiles:
    if ".png" in file:
        im = Image.open("tatkal-output/"+file)
        pixels = list(im.getdata())
        width, height = im.size
        pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

        with open('tatkal-output/'+file[:-4]+'.csv', 'wb') as csvfile:
            w = csv.writer(csvfile, delimiter=',', quotechar='|',
                           quoting=csv.QUOTE_MINIMAL)
            for row in pixels:
                data = []
                for pix in row:
                    data.append(int(bool(pix[3])))
                w.writerow(data)
