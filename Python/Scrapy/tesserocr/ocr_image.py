import tesserocr
from PIL import Image

# 利用Image读取图片，并识别图片中的验证码
image = Image.open('image.png')
print(tesserocr.image_to_text(image))