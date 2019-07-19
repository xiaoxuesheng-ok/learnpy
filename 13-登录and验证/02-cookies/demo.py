

# 保存 +  read

#  http://www.santostang.com/wp-login.php

#  注意 账号密码的name, 还有submit里边一些hiden的内容

import requests

session = requests.session()

post_url = 'http://www.santostang.com/wp-login.php'

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

headers = {

    'Host': 'www.santostang.com',
    'Origin': 'http://www.santostang.com',
    'Referer': 'http://www.santostang.com/wp-login.php',
    'User-Agent' : agent
}

postdata = {
    'pwd':'a12345',
    'log':'test',
    'rememberme':'forerver',
    'redirect_to': 'http://www.santostang.com/wp-admin/',
    'testcookie':'1'
}


login_page = session.post(post_url,data = postdata,headers = headers)

print(login_page.status_code)

#  获取cookies
print(login_page.cookies.get_dict())

#  

'''
303 重定向
400 请求错误
401 未授权
403 禁止访问
404 文件未找到
500 服务器错误
'''
