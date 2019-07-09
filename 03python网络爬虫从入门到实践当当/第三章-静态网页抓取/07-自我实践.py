
import requests

from bs4 import BeautifulSoup

def get_movies() :
    movie_list = []
    headers ={
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }


    for i in  range(0,10) :
        link = "https://movie.douban.com/top250?start="+str(i*25)

        r = requests.get(link,headers = headers,timeout = 10)

        #print(r.status_code)

        soup = BeautifulSoup(r.text,"lxml")

        div_list =  soup.find_all('div',class_="info")


        for each in div_list :

           movie = "片名：" + str(each.find('div',class_="hd").a.span.text.strip()) + "   评分：" + str(each.find('div',class_="bd").div.find(class_="rating_num").text.strip())
           movie_list.append(movie)

    return movie_list

movies = get_movies()

for movie in movies :
    print(movie)
