import time

class Semaphore:
    def __init__(self, value):
        self.value = value

    def wait(self):
        while self.value <= 0:
            print("Busy Wait")
            pass
        self.value -= 1

    def signal(self):
        self.value += 1

if __name__ == "__main__":
    buffer_size = 10
    mutex = Semaphore(1)
    empty = Semaphore(buffer_size)  
    full = Semaphore(0)
    buffer = []
    
    # Allow some time for producers and consumers to run
    time.sleep(5)

