import pytesseract

from PIL import Image
# 创建图片对象
img = Image.open('test4.jpg')
# 图像转字符串
s = pytesseract.image_to_string(img)
s_boxes = pytesseract.image_to_boxes(img)
s_data = pytesseract.image_to_data(img)
print(s)
