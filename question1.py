from threading import *
import time

class MyThread(Thread):
    def run(self):
        print('it will sleep for 5 seconds')
t = MyThread()
t.start()
time.sleep(5)
print('final output')