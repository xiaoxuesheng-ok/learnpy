import requests
r = requests.get('http://www.santostang.com')
# encoding，文本 编码
print("文本编码",r.encoding)
#  status_code，检测响应码。200正常，4XX客户端错误，5XX服务端
print("响应状态码",r.status_code)
#r.text 是服务器响应的内容，会自动根据响应头部的字符编码进行解码
print("  字符串方式的响应体：",r.text)
print("*"*10+'/n')
print(r.content)
# r.content 字节方式的响应体，会自动解码gizp和delfate编码的响应 数据。

# r.json()  requests 内置的JSON解码器
