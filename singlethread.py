import threading


lock = threading.Lock()


def func(lock):
    x=3
    lock.acquire()
    lock.acquire()
    print(x)
    lock.release()

t1 = threading.Thread(target = func, args=(lock,))
t1.start()
t1.join()
