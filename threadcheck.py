import time
import math

import threading as th


def ioutil():
    start_time=time.time()
    for x in range(0,2500):
        print(x)
    print("--- %s seconds 1 ---" % (time.time() - start_time))
        

def ioutil2():
    start_time=time.time()
    for x in range(0,2500):
        print(x)
    print("--- %s seconds  2---" % (time.time() - start_time))
    
def cpuutil():
    total=0
    start_time=time.time()
    for x in range(0,500000):
        total=total+math.factorial(x)
    print("--- %s seconds 3---" % (time.time() - start_time))
        





start_time = time.time()
t1=th.Thread(target=ioutil)
t2=th.Thread(target=cpuutil)
t3=th.Thread(target=ioutil2)
t1.start()
t2.start()
t3.start()


print("--- %s seconds ---" % (time.time() - start_time))
