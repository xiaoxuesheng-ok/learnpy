from PIL import Image
import pytesseract

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # 为图像设置一个阈值过滤器并保存
    # 如果 x < 143  返回 0 ， x >= 143 返回255
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)
    return image

image = cleanFile(r'C:\learnpy\10-NumPy\textBad.png', r'C:\learnpy\10-NumPy\textCleaned.png')

# 调用Tesseract对新创建的图像进行OCR识别
print(pytesseract.image_to_string(image))
