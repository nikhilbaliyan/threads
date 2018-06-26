from threading import *
import time
def Time(num):
    for n in num:
        time.sleep(2 * n)
        print('double: ', n)
num = [1, 2, 3, 4, 5]
t1 = Thread(target=Time, args=(num,))
t1.start()




