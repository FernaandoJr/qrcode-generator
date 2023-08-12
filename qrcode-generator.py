import qrcode
from qrcode.image.styledpil import StyledPilImage

value = input(str("Insira o conteúdo para gerar um QR Code: "))

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=1,
)
qr.add_data(value)

img = qr.make_image(image_factory=StyledPilImage,embeded_image_path=".\img\pyy-logo.png")

img.save(".\img\qrcode.png")

print("Imagem gerada com sucesso!")