from  random  import uniform,randint
from threading import Condition,Thread
from time import sleep

condition = Condition()

def produce(list):
    condition.acquire()
    while True:
        for i in range(randint(2,10)):
            num = i
            list.append(num)
            print("Produced : =>",num)

        sleepnum = randint(2,4)
        print(f"Notifying Consumer in {sleepnum} sec")
        sleep(sleepnum)
        condition.notify()
        print("notified consumer")
        condition.wait()
        print("After wait Producer code continues from here only")

    

def consume(list):
    condition.acquire()
    while True:
        num = list.pop()
        print("Consumed : =>",num)
        sleepnum = randint(2,4)
        print(f"Notifying Producer in {sleepnum} sec ")
        sleep(sleepnum)
        condition.notify()
        condition.wait()
        

itemlist = []

producer = Thread(target=produce,args=(itemlist,))
consumer = Thread(target=consume,args=(itemlist,))

producer.start()
consumer.start()


"""
Python Doc : 

acquire(blocking=True, timeout=- 1)
Acquire a lock, blocking or non-blocking.
When invoked without arguments: if this thread already owns the lock, increment the recursion level by one, and return immediately. Otherwise, if another thread owns the lock, block until the lock is unlocked. 
Once the lock is unlocked (not owned by any thread), then grab ownership, set the recursion level to one, and return.

The notify() method wakes up one of the threads waiting for the condition variable, if any are waiting. 
The notify_all() method wakes up all threads waiting for the condition variable

Note: the notify() and notify_all() methods don't release the lock; this means that the thread or threads awakened will not return from their wait() call immediately, 
but only when the thread that called notify() or notify_all() finally relinquishes ownership of the lock.

The wait() method releases the lock, and then blocks until another thread awakens it by calling notify() or notify_all().
Once awakened, wait() re-acquires the lock and returns

Pyhton Doc End;

Some sources to read
url : https://docs.python.org/3/library/threading.html#:~:text=The%20wait()%20method%20releases,acquires%20the%20lock%20and%20returns.
url : https://stackoverflow.com/questions/46076186/why-does-python-threading-condition-notify-require-a-lock


So we use 
(1) : => acquire() : to acquire a lock 
(2) : => notify()/notify_all() : to wake up the wait() on other thread 
Now  But the other thread is wake up but the current thread has acuired lock currently so the other thread can't acquire the lock
(3) : => The wait() in current lock thread will release the lock from the current thread and will move the current thread in waiter list
queue and now the other thread can acquire lock 
"""




