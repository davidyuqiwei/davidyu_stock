import os
import time
num = 0
# fork函数在windows不支持
pid = os.fork()

if pid == 0:
    num += 1
    print("全局变量num=%d" % num)
else:
    time.sleep(1)
    num += 1
    print("全局变量num=%d" % num)
