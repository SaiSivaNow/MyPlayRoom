import threading
import time
x = 0
def incre(lock):
    global x
    for y in range(0,5):
        lock.acquire()
        time.sleep(2)
        x+=1
        time.sleep(1)
        lock.release()

        
def print_sync(lock):
    prev = x
    while True:
        lock.acquire()
        print(x)
        time.sleep(1)
        lock.release()
        


lock = threading.Lock()
t_one = threading.Thread(target=incre,args=(lock,))
t_two = threading.Thread(target=print_sync,args=(lock,))

t_two.start()
t_one.start()
t_one.join()
t_two.join()
