# 生成器
# 在python中，一边循环一边计算的机制，称为生成器：generator
# 创建方法1 只要把[]变成()
l = [x * 2 for x in range(5)]
print(l)    # [0, 2, 4, 6, 8]
k = (x * 2 for x in range(5))
print(k)    # <generator object <genexpr> at 0x7fb359190cf0>
# 可以通过next for list等方法使用
# print(list(k))  # [0, 2, 4, 6, 8]
print(next(k))  # 0
print(next(k))  # 2
print(next(k))  # 4
print(next(k))  # 6
print(next(k))  # 8

# 创建方法2 有yield关键字就称为生成器
# 用生成器实现斐波那契数列
def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a    # 相当于返回值是a，循环n次
        # 然后把列表里面所有的数据都返回回来
        a, b = b, a+b

F = fib(9)      # F是生成器对象
for i in F:     # 按照使用迭代器的方式来使用生成器
    print(i)    # 0 1 1 2 3 5 8 13 21
# 使用了yield关键字的函数不再是函数，而是生成器
# yield关键字有两个作用
# 保存当前运行状态(断电)，然后暂停执行，将生成器(函数)挂起
# 将yield关键字后面表达式的值作为返回值返回，起到return的作用
# 可以使用next()函数让生成器从断电处继续执行，唤醒生成器

# 使用send唤醒
# 用send唤醒的好处是可以向断点处传入一个附加数据
def gen():
    c = 0
    while c < 5:
        temp = yield c
        print(temp)
        c += 1

f = gen()
# next(f)     # 第一次迭代生成器时，不能使用带参数的send来迭代，可以用next或者用send(None)
# f.send('111')   # can't send non-None value to a just-started generator
f.send(None)
f.send('hahaha')    # hahaha
next(f)     # None

# 装饰器
"""
闭包
1.函数嵌套
2.外部函数返回内部函数的名字，即函数的引用
3.内部函数可以使用外部函数的参数，即自由变量
"""
def out(num):
    def inner():
        print(f'{num}次')
        return 'haha'
    return inner

a = out(10)     # 调用out 返回值复制给a
a()     # 10次
result = a()
print(result)       # 10次   haha

"""
自定义装饰器-->闭包
@外部函数的名字
被装饰的函数
装饰器的作用：在不改变原来函数代码的基础上，给其增加新的功能
"""
# 需求：不改变原函数的代码前提下，判断用户是否已经登陆
def is_login(func):
    def _login():
        print('您是合法用户，请开始您的操作')
        func()
    return _login

@is_login
def query():
    print('欢迎您')
    print('您的余额是¥500')

# a = query()
a()    # 您是合法用户，请开始您的操作 欢迎您 您的余额是¥
"""
装饰器
被装饰的函数--内部实现原来功能
被装饰的函数的名字 = 闭包外部函数的名字(被装饰的函数的名字)()
"""
# query = is_login(query)   # query = _login 被装饰的函数现在指向了内部函数的应用
# query()

# 多层装饰器
def start(func):
    def _start():
        return '<p>' + str(func()) + '</p>'
    return _start

def end(func):
    def _end():
        return '<div>' + str(func()) + '</div>'
    return _end

@end
@start
def query():
    return '我是多层装饰器'    # 先用离得近的，再用离得远的装饰器


print(query())  # <div><p>我是多层装饰器</p></div>

# 通用装饰器
"""
有无参数和返回值都可以用
需求：统计函数的运行效率的装饰器
"""
import time
from functools import wraps

def start(func):
    @wraps(func)
    def _start(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'操作用时{end_time-start_time}')
        return result
    return _start

@start
def query(a, b):        # 没有参数和返回值，也可以得到运行时间
    time.sleep(1)
    sum = a + b
    return sum


print(query(10, 20))    # 操作用时1.002601146697998     30

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         n = len(l1)
#         m = len(l2)
#         a, b = 0, 0
#         for i in range(n):
#             a += l1[i]*pow(10, i)
#         for j in range(m):
#             b += l2[j]*pow(10, j)
#         c = a + b
#         d = [int(x) for x in str(c)]
#         d.reverse()
#         return d
# Solution.addTwoNumbers(self=,l1=[2,4,3,1], l2=[5,6,4])

# 带参数的装饰器
# 两层的时候，最外层的函数只能接受被装饰的函数的名字作为参数，进行传参,内部函数其实就是被装饰后的函数最后运行的代码逻辑
# 需求：装饰器作用：不想更改query函数的代码的前提下，增加判断用户是否登陆成功这个功能
def is_login(flag):
    def out(func):
        def inner():
            if flag == 'success':
                print('登陆成功！')
                # 进行余额查询
                func()
            else:
                print('请跳转到登陆页面')
        return inner
    return out

@is_login('success')
def query():
    print('欢迎您')
    print('您的余额是¥2000')

query()     # 登陆成功！欢迎您 您的余额是¥2000

# 类装饰器
'''
类也可以写成装饰器，魔法方法的辅助
__call__() 就是让对象具有函数的功能，可以像函数一样通过对象()被调用
'''
class Screen(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, func): # 当作外部函数
        # 把函数的名字当作参数传递进来
        def inner(*args):
            print(self.name)
            print('------')
            func()
        return inner

@Screen('yaoyao')
def query():
    print('欢迎您')
    print('您的余额是¥2000')


query()     # yaoyao    ------  欢迎您 您的余额是¥2000

# 多任务
# 多线程代码实现 threading模块
import threading
from time import sleep,ctime
def sing():
    for i in range(3):
        print('正在唱歌...%d'%i)
        sleep(1)
def dance():
    for i in range(3):
        print('正在跳舞...%d'%i)
        sleep(1)

t1 = threading.Thread(target=sing)
t2 = threading.Thread(target=dance)
t1.start()
t2.start()          # 正在唱歌...0  正在跳舞...0    正在唱歌...1    正在跳舞...1    正在唱歌...2    正在跳舞...2

# 多进程代码实现   multiprocessing模块,process代表一个进程对象
# from multiprocessing import Process
# from time import sleep
#
# def run_proc(name, age, **kwargs):
#     for i in range(10):
#         print('子进程运行中，name = %s, age = %d,' % (name, age))
#         print(kwargs)
#         sleep(0, 2)
#
# if __name__ == '__main__':
#     p = Process(target=run_proc, args=('test', 18), kwargs={"m": 20})
#     p.start()
#     p.join()

# 进程不共享全局变量
# from multiprocessing import Process
# import os
# import time
#
# nums = [11, 22]
#
# def work1():
#     """子进程要执行的代码，os.getpid()获取进程的pid"""
#     print("in process1 pid=%d, nums=%s" % (os.getpid(), nums))
#     for i in range(3):
#         nums.append(i)
#         time.sleep(1)
#         print("in process1 pid=%d, nums=%s" % (os.getpid(), nums))
#
# def work2():
#     """子进程要执行的代码"""
#     print("in process2 pid=%d, nums=%s" % (os.getpid(), nums))
#
# if __name__ == '__main__':
#     p1 = Process(target=work1)  # target值的是你要执行的任务
#     p1.start()
#     p1.join()
#     # 告诉其他进程 你要等我完成工作之后 你再工作 需要等待的进程用join()
#     p2 = Process(target=work2)
#     p2.start()

# 线程的资源竞争
import threading
import time
g_num = 0
# 创建锁
# mutex = threading.Lock()

def work1(num):
    global g_num
    for i in range(num):
        # # 上锁
        # mutex.acquire()
        # g_num += 1
        # # 释放锁
        # mutex.release()
    print("----in work1, g_num is %d----" % g_num)
print("---线程创建之前g_num is %d" % g_num)   # ----in work1, g_num is 100000----

def work2(num):
    global g_num
    for i in range(num):
        # # 上锁
        # mutex.acquire()
        # g_num += 1
        # # 释放锁
        # mutex.release()
    print("----in work2, g_num is %d----" % g_num)
print("---线程创建之前g_num is %d" % g_num)   # ----in work1, g_num is 154073----
# 没有等work1运行完，就已经在运行，所以没有到200000
# 加了锁之后，就可以到200000

t1 = threading.Thread(target=work1, args=(100000,))
t1.start()

t2 = threading.Thread(target=work2, args=(100000,))
t2.start()

while len(threading.enumerate()) != 1:
    time.sleep(1)

print("2个线程对同一个全局变量操作之后的最终结果是：%s" % g_num)
"""
备注：
Process和Thread都有以下参数：
Process创建的实例对象的常用方法
start():启动子进程实例(创建子进程)
join([timeout])：是否等待子进程执行结束，或等待多少秒
Process()
target:如果传递了函数的应用，可以认为这个子进程就是执行这里的代码
args:给target指定的函数传递的参数，以元组的方式传递
kwargs:给target指定的函数传递命名参数
"""
