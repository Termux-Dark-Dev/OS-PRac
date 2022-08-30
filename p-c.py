
#    Producer Consumer Problem Using Shared Memory

import threading as th
from time import sleep
import random

def produce(itemlist):
    i = 0
    while True:
        sleep(random.uniform(0,2))                  # random.uniform generates a no btwn 0 => min , 2 => max  
        itemlist.append(i)
        print("Produced : ",i)
        i += 1

def consume(itemlist):
    while True:
        sleep(random.uniform(0,2))
        if(len(itemlist)==0):
            print("List is empty")
            continue
        item = itemlist.pop(0)
        print("Consumed :",item)

items = []
producer = th.Thread(target=produce,args=(items,))
consumer = th.Thread(target=consume,args=(items,))


producer.start()
consumer.start()