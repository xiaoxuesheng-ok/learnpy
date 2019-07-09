import requests

from lxml import etree

link = "http://wwww.santostang.com/"

r = requests.get(link)

html = etree.HTML(r.text)
#html = BeautifulSoup(r.text,'LXML')

title_list = html.xpath('')
