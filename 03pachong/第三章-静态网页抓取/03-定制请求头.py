# headers提供了关于请求、响应或其他发送实体的信息
# 01 先访问目标网站，通过chrome 右键检查，networ 获取需要的头部信息。


import requests

headers = {
 'Host': 'www.santostang.com',
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
 }

r = requests.get('http://www.santostang.com/',headers = headers)

print(r.status_code)
