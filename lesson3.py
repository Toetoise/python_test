# # 石头剪刀布游戏
# import  random
# c = ['石头', '剪刀', '布']
# while True:
#     a = input('请出拳0-拳 1-刀 2-布，或者退出游戏(q):')
#     if a in ['0', '1', '2']:
#         a = int(a)
#         b = random.randint(0, 2)
#         if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 or b == 1):
#             print(f'玩家出{c[a]},电脑出{c[b]},玩家胜')
#         elif a == b:
#             print(f'玩家出{c[a]},电脑出{c[b]},平局了')
#         else:
#             print(f'玩家出{c[a]},电脑出{c[b]},电脑胜')
#     elif a in ['q', 'Q']:
#         d = input('确定要退出游戏么(y/n)：')
#         if d == 'y' or d == 'Y':
#             print()
#         break
#     else:
#         print('您输入错误，请重新输入')


# 九九乘法表
# 用父循环把九行打出来 while循环
a = 1
while a <= 9:
    # print(f'我是第{a}行')
    # todo 完善每一行的内容
    col = 1
    while col <= a:
        print(f'{col}*{a}={col*a}', end='\t')
        col += 1
    print()
    a += 1
# 用for循环
for a in range(1, 10):
    for col in range(1, a+1):
        print(f'{col}*{a}={col*a}', end='\t')
    print()

# 退出循环的方式
# while..else
# while..break..else
# while..continue..else
# for..else
# for..break..else
# for..continue..else

# 函数
# 定义函数>调用函数
# def 函数(参数) > 函数(参数)


def s1(b, c):
    d = b + c
    print(d)


s1(3, 4)    # 7


def s2():
    """
    三个单引号或双引号之间是对函数的解读
    :return:
    """
    return 404  # return也代表了函数的终止，函数内return后面的代码不会被执行
    print('这个函数结束了')


n = s2()    # n代表函数s2的返回值，如果n值等于None，证明这个函数没有返回值
print(n)    # 404
print(s1(3, 4))     # 7 None(因为没有返回值，先会打印函数的结果，然后返回值为None)


def print_one_line():
    print('-'*10)


print_one_line()    # ----------


def print_lines(n):
    i = 1
    while i <= n:
        print_one_line()
        i += 1


print_lines(5)


# 函数题内部修改全局变量的值，通过global去声明该变量,并且执行该函数
a = 3


def s3():
    global a
    a = 5
    print(a)


s3()
print(a)

# 函数的参数
# 1.位置参数
def user_info(name, age, gender):
    print(f'您的姓名是{name},年龄是{age},性别是{gender}')


user_info('tortoise', 25, '男')      # 您的姓名是tortoise,年龄是25,性别是男
# 2.关键字参数 函数调用，通过'键=值'形式加以指定
def user_info(name, age, gender):
    print(f'您的姓名是{name},年龄是{age},性别是{gender}')


user_info(gender='女', age=17, name='zouzou')        # 您的姓名是zouzou,年龄是17,性别是女
# 函数调用时，如果有位置参数，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
# 3.缺省参数 也叫默认参数，用于定义函数，为函数中的参数提供默认值，调用时可不传该参数的值(在函数定义和调用时，所有位置参数必须出现在默认参数前)
def user_info(name, age, gender='女'):
    print(f'您的姓名是{name},年龄是{age},性别是{gender}')


# 调用函数，使用默认参数，不传gender
user_info('zouzou', 18)     # 您的姓名是zouzou,年龄是18,性别是女
# 调用函数，修改默认参数的值,关键字参数不区分顺序，只要在位置参数的后面就可以
user_info('tom', gender='男', age=20)    # 您的姓名是tom,年龄是20,性别是男
# 4.不定长参数：可变参数，用于不确定调用的时候会传递多少个参数(不传也可以)，可用包裹位置参数或关键词参数来进行参数传递，会非常方便
# a.包裹位置参数传递  *args  对元组进行解包 * 解包
def user_info(*args):
    print(args)


# 定义函数时有*args 调用函数用位置参数
user_info('Tom')    # ('Tom',)
user_info()     # ()
user_info('Tom', 90)    # ('Tom', 90)
# b.包裹关键词参数传递   **kwargs  字典形式的  ** 解包 kwargs
def user_info(**kwargs):
    print(kwargs)


# 定义函数有**kwargs 调用函数用关键词参数
user_info(name='Tom', age=25, gender='男')       # {'name': 'Tom', 'age': 25, 'gender': '男'}

# 拆包
# 元组拆包 对应参数
# 字典拆包 对应key

# 可变和不可变的数据类型(数据能否直接修改)
# 可变    列表 字典 集合
# 不可变   整数 字符串 元组

def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)  # [10]
print("list1=%s"%list1)     # [10]
list2 = extendList(123, [])     # [123]  ==>  list2 = extendList(123, list=[])重新定义了后面的参数值
list3 = extendList('a')     # [10, 'a']
print("list1=%s"%list1)     # [10, 'a']
print("list2=%s"%list2)     # [123]
print("list3=%s"%list3)     # [10, 'a']

# lambda语法   =匿名函数   如果一个函数只有一个返回值，并且只有一句代码，可以使用lambda进行简化
# lambda 参数：表达式
# lambda表达式的参数可有可无，函数的参数在lambda中完全适用
# lambda函数能接收任意数量的参数，但只能返回一个表达式的值
# 支持无参数，一个参数，默认参数，可变参数*args，可变参数**kwargs
print((lambda a, b: a + b)(10, 20))     # 30
fn = lambda a, b, c=100: a+b+c
print(fn(40, 20))    # 160
print((lambda a, b: True if a > b else False)(100, 150))   # False

students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'jack', 'age': 24}
]
# 列表序列.sort(key=None,reverse=False) 默认是升序
students.sort(key=lambda x:x['name'])
print(students)     # [{'name': 'ROSE', 'age': 19}, {'name': 'TOM', 'age': 20}, {'name': 'jack', 'age': 24}]
students.sort(key=lambda x:x['name'], reverse=True)
print(students)     # [{'name': 'jack', 'age': 24}, {'name': 'TOM', 'age': 20}, {'name': 'ROSE', 'age': 19}]
students.sort(key=lambda x:x['age'])
print(students)     # [{'name': 'ROSE', 'age': 19}, {'name': 'TOM', 'age': 20}, {'name': 'jack', 'age': 24}]

# 高阶函数
# 需求：一个函数完成两个任意数字的绝对值只和 abs()绝对值
def add_num(a, b):
    return abs(a) + abs(b)
print(add_num(1,-4))    # 5

def add_nums(a, b, f):
    return f(a) + f(b)
print(add_nums(-3, 5, abs))   # 8
# 函数式编程大量使用函数，减少了代码的重复，因此程序比较短，开发速度快

# 内置高阶函数
# 1.map()会根据指定的函数对指定序列做映射
# 第一个参数function()以参数序列的每一个元素调用function函数，返回包含每次function函数返回值的新列表。如果要转换为列表，可以使用list()来转换
# 语法：   map(function, iterable,....)
# 参数：   function:函数 iterable：一个或多个序列
# 返回值：  python3返回的是迭代器
list1 = [7, 10, 13, 2]
result = map(lambda x: x*2, list1)
print(result)   # <map object at 0x7f8e01109130>
list2 = list(result)
print(list2)    # [14, 20, 26, 4]

# 2.reduce()
# reduce(func(x, y), list)函数会对参数序列中元素进行积累。其中func必须有两个参数，每次func计算的结果继续和序列的下个元素做继续计算
# a.reduce()传入的参数func必须接收2个参数
# b.reduce是要从functions里面去导包的
# 需求：计算list1序列中各个数字的累加和
from functools import reduce
list1 = [3, 5, 6, 4, 7]
result = reduce(lambda x, y: x+y, list1)
print(result)   # 25

# 3.filter()
# filter(func, list)函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。如果要转换为列表，可以使用list()来转换
# 需求：筛选出列表里面的偶数项
list2 = [1, 2, 2, 3, 4, 7, 14, 6]
print(list(filter(lambda x: x % 2 == 0, list2)))    # [2, 2, 4, 14, 6]
def func(x):
    return x % 2 == 0
result = filter(func, list2)
print(result)   # <filter object at 0x7fcaff109100>
print(list(result))     # [2, 2, 4, 14, 6]


