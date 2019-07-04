#导入参数模块
from sys import argv

# 接收参数
script, filename = argv

#打开文件
text = open(filename)

#打印
print(f"Here's your file {filename}")
# 读取文件
print(text.read())
text.close()
#打印
print("Type the filename again:")
#输入文件路径
file_again = input(">")

# 读取文件
text_again = open(file_again)
#再次打印文件
print(text_again.read())
text_again.close()
