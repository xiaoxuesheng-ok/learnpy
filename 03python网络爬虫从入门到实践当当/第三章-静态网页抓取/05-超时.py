import requests
link = "http://www.santostang.com/"
r = requests.get(link,timeout = 20)


#默认超时为20秒, timeout = 2 ,表示2秒。
