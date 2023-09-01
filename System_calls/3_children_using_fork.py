import os
import time

class Proc:
	def __init__(self):
		pi = os.fork()

	def o_e(self,n):
		if n%2 == 0:
			print("Even")
		else:
			print("Odd")
	
	def sum(self,n):
		print("Sum:",(n*(n+1))/2))

	def pal(self,n):
		if str(n) == str(n)[:-1]:
			print("Palindrome")
		else:
			print("Not Palindrome")
		

	if pid :
    		status = os.wait()
    		print("\nParent process running...")
    		print("Terminated child's process id:", status[0])
    		print("Signal number that killed the child process:", status[1])

	else :
    		print("Child process running....")
    		print("Process ID:", os.getpid())
    		print("Exiting")
   
if __name__ == "__main__":
	p = Proc()
	
