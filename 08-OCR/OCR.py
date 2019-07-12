from PIL import Image
import pytesseract
from pytesseract import Output

# 图像的 OCR 结果
print(pytesseract.image_to_string(Image.open(r'C:\learnpy\08-OCR\image.png')))


# 返回所有数据的完整输出，例如置信分数、页数、行数、像素位置数据以及其他信息
print(pytesseract.image_to_boxes(Image.open(r'C:\learnpy\08-OCR\image.png')))


#它可以估计边界（每个字符的边界的像素位置）：
print(pytesseract.image_to_data(Image.open(r'C:\learnpy\08-OCR\image.png')))

# 默认情况下，最后两个输出文件是用空格或 tab 分隔的字符串文件，
# 但是你也可以输出字典，或者在不能够进行 UTF-8 解码的情况下输出字节字符串：
print(pytesseract.image_to_data(Image.open(r'C:\learnpy\08-OCR\image.png'),
    output_type=Output.DICT))

print(pytesseract.image_to_string(Image.open(r'C:\learnpy\08-OCR\image.png'),
    output_type=Output.BYTES))
