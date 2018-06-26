from threading import *
import time
n=int(input("enter the number"))
def factorial(n):
    num=n
    if num < 1:
        return 1
    else:
	    return num * factorial(num - 1)
t = Thread(target=factorial,args=(n,))
t.start()
print("process id being executing")
print(factorial(n))