from PIL import Image
import mechanize
from StringIO import StringIO
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

for i in range(509, 510):
    r = br.open('https://www.irctc.co.in/eticketing/captchaImage')
    im = Image.open(StringIO(r.read()))
    im.save("tatkal/"+str(i+1)+".png")
    print "Saving: tatkal/"+str(i+1)+".png"
