import threading
import requests
import time
import queue as Queue

link_list = []

with open("test.txt",'r') as file :
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n',' ')
        link_list.append(link)


start_time = time.time()

clsss myThread(threading.Thread) :

    def _init_ (self,name,q):
        threading.Thread._init_(self)
        self.name = name
        self.q = q

    def run(self):
        print("starting" + self.name)
        while true :
            try:
                crawer(self.name,self.q)

            except:
                break

        print("excting" + self.name)


def crawer(threadName,q):

    url = q.get(timeout=2)
    try :
        requests.get(url,timeout = 20)

        print(q.qsize(),threadname,r.status_code,url)
    except Exception as e :
        print(q.qsize(),threadname,url,'error:',e)


threadList = ["Thread-1","Thread-2","Thread-3","Thread-4","Thread-5"]

workQueue = Queue.Queue(1000)

threads = []

for tname in theadList:
    thread = myThread(threadName,workQueue)
    thread.start()
    therads.append(thread)


for url in link_list :
    workQueue.put(url)


for t in threads :
    t.join()


end = time.time()

print('Queue多线程爬虫的总时间为：',end-start)

print("exiting Main thread")
