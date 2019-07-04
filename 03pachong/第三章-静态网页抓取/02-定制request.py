import requests
key_dict = {'key1':'value1','key2':'value2'}
r= requests.get("http://httpbin.org/get",params = key_dict)
print(r.url)
print(r.text)
