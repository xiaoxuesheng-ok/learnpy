from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def get_name(html):
    try:
        bs = BeautifulSoup(html, 'html.parser')
        for link in bs.find('div', {'id':'bodyContent'}).find_all(
            'a', href=re.compile('^(/wiki/)((?!:).)*$')):
            if 'href' in link.attrs:
                print(link.attrs['href'])
    except:
        get_name(html)

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")

get_name(html)
