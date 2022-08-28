import pyqrcode
import png

#simple qrcode transformer just to learn

c = input("What do you want to transform in a QRCode: (1) text (2) Url (3) file directory")

if int(c) == 1:
    text = pyqrcode.create(input("Enter a text:"))
    q = int(input("Do you want to change qrcode name: (1) yes (2) no"))
    if q == 1:
        pngname = input("Enter a name for your qrcode:")
        text.png("{}.png".format(pngname), scale=8, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    else:
        text.png('text.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])

# url = pyqrcode.create(input("Enter a text to transform in a QRCode:"))
# url.svg("code.svg", scale = 8)
# print(s.terminal(quiet_zone=1))
# url.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
