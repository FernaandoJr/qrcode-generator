import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask

value = input(str("Insert a link or text: "))

qr = qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=1,
)
qr.add_data(value)

img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path=".\img\logo.png",
    color_mask=SolidFillColorMask(back_color=(255,255,255), front_color=(19, 17, 15))
)

img.save(".\img\qrcode.png")
print(f"\nQR Code successfully generated!\n")