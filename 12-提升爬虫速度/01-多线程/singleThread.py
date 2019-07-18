
#  代码并不能运行，及供参考单线程含义。

import requests
import time

COMMENT_FILE_PATH = 'singleThread.csv'

link_list = []

with open(COMMENT_FILE_PATH,'r') as file :
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.repace('\n',' ')
        link_list.append(link)


start = time.time()
for eachone in link_list :
    try:
        r = requests.get(eachone)
        print(r.status_code,eachone)
    except Exception as e :
        print("Error:",e)

end = time.time()

print('串行的总时间为：'，end-start)
