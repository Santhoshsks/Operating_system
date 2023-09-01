import os
import time

pid = os.fork()

if pid :
    status = os.wait()
    print("\nParent process running...")
    print("Terminated child's process id:", status[0])
    print("Signal number that killed the child process:", status[1])
 
else :
    print("Child process running....")
    print("Process ID:", os.getpid())
    print("Exiting")
