import time

def timeyu(func):
    print(time.time())
    return func()

@timeyu  # 从这里可以看出@time 等价于 time(xxx()),但是这种写法你得考虑python代码的执行顺序
def xxx():
    print('Hello world!')


def foo(x,*args,y=1):
    print(x)
    print(y)
    print(args)
foo(1,[3,4,4,5,6,7],y=3)
