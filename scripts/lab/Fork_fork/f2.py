import os
from time import sleep

pid = os.fork()
pid2 = os.fork()

if pid <0 :
    print("create process failed")
    print(pid)
elif pid == 0:
    sleep(3)
    print("this is child process")
    print(os.getpid())
elif pid2 ==0:
    sleep(4)
    print("this is child process2")
    print(os.getpid())
else:
    sleep(1)
    print("this is parent process")
    print(pid)

print("******the end*******")
