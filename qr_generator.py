# commands to run
# pip install pillow
# pip install qrcode

import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=100,
    border=1
)

qr.add_data("https://linktr.ee/mahmoudbasma")
qr.make(fit=True)

#for colors you can use:
# 1.A string representing a color name (e.g., "black", "red", "blue").
# 2.A tuple of RGB values (e.g., (0, 0, 0) for black, (255, 0, 0) for red).
# 3.A string representing the hex code (e.g., "#32417F" for light blue)

img = qr.make_image(fill_color="white", back_color="#091366")
img_pil = Image.frombytes(img.mode, img.size, img.tobytes())
img_pil.save("dark_blue_qr.png", dpi=(300, 300))

