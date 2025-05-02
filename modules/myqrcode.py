# import qrcode

# data = qrcode.make("https://jaro-website.s3.ap-south-1.amazonaws.com/2024/06/Pattern-Programs-in-C.jpg")

# type(data)

# data.save("new_qr.png")

# print("qrcode created")


import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("my_qr.png")