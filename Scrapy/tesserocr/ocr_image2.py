import tesserocr
from PIL import Image

# 利用Image读取图片，并识别图片中的验证码
image = Image.open('image2.png')

# 参数L,将图片转化为灰度图片
image = image.convert('L')
threshold = 127
table = []

# 指定二值化的阀值， 处理后图片会变得黑白分明
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
image.show()

result = tesserocr.image_to_text(image)
print(result)
