from multiprocessing import Process
from multiprocessing import Pipe
import os, time

def parent_function(parent_number,pipe_r,pipe_w):
    pid = os.fork()
    if pid > 0:
        print(f"Parent {parent_number}")
        pid1 = os.getpid()
        print(f"PID: {pid1}")
        ppid = os.getppid()
        print(f"PPID: {ppid}\n")
        msg = f"Hello child, I am Child {parent_number}'s parent\n"
        print(f'P{parent_number} is sending : {msg}')
        pipe_w.send(msg)
        time.sleep(1)
    else:
        child_function(parent_number,pipe_r)

def child_function(child_number,pipe_r):
    print(f"This is child {child_number}")
    pid = os.getpid()
    print(f"PID: {pid}")
    ppid = os.getppid()
    print(f"PPID: {ppid}\n")
    msg = pipe_r.recv()
    print(f'C{child_number} received : {msg}')

if __name__ == "__main__":

    pipe_r1, pipe_w1 = Pipe()
    pipe_r2, pipe_w2 = Pipe()

    parent1_process = Process(target=parent_function, args=(1,pipe_r1,pipe_w2))
    parent2_process = Process(target=parent_function, args=(2,pipe_r2,pipe_w1))
    parent1_process.start()
    parent1_process.join()
    parent2_process.start()
    parent2_process.join()


