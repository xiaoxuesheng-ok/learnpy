import threading
import time

class myThread(threading.Thread):
    def _init_(self,name,delay):
        threading.Thread._init_(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting"+self.name)
        print_time(self.name,self.delay)
        print("Exiting" + self.name)


def print_time(threadName,delay):
    counter = 0
    while counter < 3 :
        time.sleep(delay)
        print(threadName,time.ctime())
        counter += 1

threads = []

# 创建新 线程

thread1 = myThread(target = "Thread-1",args = 1)

thread2 = myThread(target = "Thread-2",args = 2)


# 开启新线程

thread1.start()

thread2.start()

# 添加线程到 线程列表

threads.append(thread1)

threads.append(thread2)


# 等待多少有线程完成

for t in threads:
    t.join()

print("Execting Main Thread ")
