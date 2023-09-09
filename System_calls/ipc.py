from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Pipe

def generate_send(connection, value, pid):
    new_value = random()
    sleep(new_value)
    value = value + new_value
    print(f'P{pid} is sending :{value}')
    connection.send(value)

def link(connection, send_first,pid):
    print("Bi Directional")
    print(f"Process {pid} Running")
    if send_first:
        generate_send(connection, 0,pid)
    while True:
        value = connection.recv()
        print(f'P{pid} received :{value}')
        generate_send(connection, value, pid)
        if value > 10:
            break
    print('Process Done')


def link1(connection, pid):
    print("Uni Directional")
    print(f"Process {pid} Running")
    while True:
        generate_send(connection, 0,pid)


def link2(connection,pid):
    print(f"Process {pid} Running")
    ans = 0
    while True:
        value = connection.recv()
        print(f'P{pid} received :{value}')
        ans += value
        if ans > 10:
            break
    print('Process Done')


if __name__ == '__main__':
    dir = int(input("Enter choice:\n 1)Uni-directional\t\t2)Bi-drectional\nChoice[1/2]:"))
    if dir == 1:
        conn1, conn2 = Pipe()
        p1 = Process(target=link1, args=(conn1,1))
        p2 = Process(target=link2, args=(conn2,2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    elif dir == 2:
        conn1, conn2 = Pipe(duplex=True)
        p1 = Process(target=link, args=(conn1,True,1))
        p2 = Process(target=link, args=(conn2,False,2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    else:
        print("Wrong choice!")