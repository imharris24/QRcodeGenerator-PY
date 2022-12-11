import qrcode

# function to get user input
def getInput():
    url = input('Enter URL or DATA to create QR-code: ')
    return url

# function to generate qr-code and return
def createQR(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# main

print('\n\tQR-CODE GENERATOR\n')

data = getInput()

QR_img = createQR(data)

# save qr-code to directory
QR_img.save('QR code.png')
