import os
import time

# Creating child processes using fork() method
a = os.fork()

if a > 0:
	print("Parent process id:",os.getpid())
	print("parent parent Process id:",os.getppid())
else:	
	
	print("Child process id:",os.getpid())
	print("Child parent Process id:",os.getppid())
