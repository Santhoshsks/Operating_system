import os

class Proc:
    def __init__(self):
        n = int(input("Enter n:"))
        pid = os.fork()

        if pid:
            status = os.wait()
            print("Terminated child's process id:", status[0])

            pid2 = os.fork()
            if pid2:
                status1 = os.wait()
                print("Terminated child's process id:", status1[0])
                
                pid3 = os.fork()

                if pid3:
                    status1 = os.wait()
                    print("Terminated child's process id:", status1[0])
                    
                    print("\n")
                    print("Parent's PID:", os.getpid())
                    print("Parent's PPID:",  os.getppid())
                else:
                    print("3- Child's PID:", os.getpid())
                    print("3- Child's PPID:",  os.getppid())
                    self.pal(n)

            else:
                print("2- Child's PID:", os.getpid())
                print("2- Child's PPID:",  os.getppid())
                self.sum(n)

                
        else:
            print("1- Child's PID:", os.getpid())
            print("1- Child's PPID:",  os.getppid())
            self.o_e(n)


    def o_e(self, n):
        if n % 2 == 0:
            print("Even\n")
        else:
            print("Odd\n")

    def sum(self, n):
        print("Sum:", (n * (n + 1)) / 2,"\n")

    def pal(self, n):
        if str(n) == str(n)[::-1]:
            print("Palindrome\n")
        else:
            print("Not Palindrome\n")

if __name__ == "__main__":
    p = Proc()
