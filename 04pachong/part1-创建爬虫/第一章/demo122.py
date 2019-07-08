from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')

#html.parser  和  lxml是两个解析器，前者是内置的。
bs = BeautifulSoup(html, 'html.parser')
print(bs.h1)
