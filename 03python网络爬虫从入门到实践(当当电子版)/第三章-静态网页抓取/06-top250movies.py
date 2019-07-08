# 01- chrome 检查请求头。
#  查看是否一个页面就可以拿到所有数据，不是的话，需要u 观察连接  规律


import requests
from bs4 import BeautifulSoup

def get_movies() :
    headers = {
      'Host':'movie.douban.com',
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }

    movie_list = []


    for i in range(0,10):
        link = "https://movie.douban.com/top250?start="+str(i*25)
        r = requests.get(link,headers = headers,timeout = 10 )
        print(str(i+1)+"页面响应状态码:",r.status_code)

        soup = BeautifulSoup(r.text,"lxml")
        div_list = soup.find_all('div', class_="hd")
        for each in div_list :
            movie = each.a.span.text.strip()
            movie_list.append(movie)

    return movie_list


movies = get_movies()
print(movies)
