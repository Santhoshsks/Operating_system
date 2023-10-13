import time
import os

class Semaphore:
    def __init__(self, value):
        self.value = value

    def wait(self):
        while self.value <= 0:
            print("Buffer Full - Busy Wait")
            time.sleep(50)
            continue
        self.value -= 1

    def signal(self):
        self.value += 1

def produce_item(item):
    item += 1
    print("Produced item:",item)
    return item

def consume_item(item):
    print("Consumed:", item)

def producer(item):
    while True:
        print("p full:",full.value)
        print("p mutex:",mutex.value)
        print("p empty:",empty.value)
        next_produced = produce_item(item)
        item = next_produced
        empty.wait()
        mutex.wait()
        buffer.append(next_produced)
        print("Buffer:",buffer)

        mutex.signal()
        full.signal()
        print("p full:",full.value)
        print("p mutex:",mutex.value)
        print("p empty:",empty.value)

def consumer():
    while True:
        print("c full:",full.value)
        print("c mutex:",mutex.value)
        print("c empty:",empty.value)
        full.wait()
        mutex.wait()

        next_consumed = buffer.pop(0)

        mutex.signal()
        empty.signal()
        print("c full:",full.value)
        print("c mutex:",mutex.value)
        print("c empty:",empty.value)

        consume_item(next_consumed)
        
if __name__ == "__main__":
    buffer_size = 10
    mutex = Semaphore(1)
    empty = Semaphore(buffer_size) 
    full = Semaphore(0)
    buffer = []
    pid = os.fork()
    if pid > 0:
        print("Producer is initialized")
        producer(0)
    else:
    	print("Consumer is initialized")
    	consumer()

