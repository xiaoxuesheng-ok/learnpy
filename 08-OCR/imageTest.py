

#   命令行调用  tesseract image.png result
#   其中第一个参数为图片名称，第二个参数result 为结果保存的目标文件名称。

#   运行结果便是图片的识别结果：Python3WebSpider。可以在chromeDownload文件夹中看到result.txt，这时已经成功将图片文字转为电子文本了。


from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open(r'C:\learnpy\08-OCR\image.png'))
print(text)
