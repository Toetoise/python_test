f = open('demo.txt', 'r')
# f.write('hello')
a = f.read()
print(a)

import os
# 绝对路径
base_path = os.path.abspath(__file__)
print(base_path)    # /Users/tortoise/PycharmProjects/python_test/lesson4.py
# 文件路径(即文件所在文件夹路径)
base_path = os.path.dirname(__file__)
print(base_path)    # /Users/tortoise/PycharmProjects/python_test
# 动态获取文件路径
# 需求：动态获取demo.txt的路径
# os.path.join(path1, path2..., filename) 把目录和文件合成一个路径
file_path = os.path.join(base_path, 'demo.txt')
print(file_path)    # /Users/tortoise/PycharmProjects/python_test/demo.txt

# 魔法方法
class Plane():

    def fly(self):
        print('飞机会飞')

b = Plane()
b.fly()
print(b)    # <__main__.Plane object at 0x7fbcf47c6fd0>

class Plane():

    def fly(self):
        print('飞机会飞')


    # 定义对象的详细信息
    def __str__(self):
        return '这是对类的说明'


b = Plane()
b.fly()
print(b)    # 这是对类的说明

class Plane():

    def __init__(self, name, color):    # 在类里面定义对象的属性    self.属性名字=值    传入对应的参数
        self.name = name
        self.color = color
    def fly(self):
        print('飞机会飞')

    # 定义对象的详细信息
    def __str__(self):
        return '这是对类的说明'

# 创建对象，对象=类名() 对象的初始化
b = Plane('Jack', 'blue')
print(b.name)   # Jack
print(b.color)  # blue
# 在类外面添加对象的属性，对象名.属性=值
b.voice = '嗡嗡嗡'
print(b.voice)  # 嗡嗡嗡
b.fly()
print(b)    # 这是对类的说明

class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具名称是{self.name},面积是{self.area}'

class House:
    def __init__(self, house_type, house_area):
        self.house_type = house_type
        self.house_area = house_area
        self.item_list = []
        self.free_area = house_area

    def add_item(self, HouseItem):
        self.item_list.append(HouseItem.name)
        if self.free_area < HouseItem.area:
            print('剩余面积太小，放不下此家具')
        else:
            self.free_area -= HouseItem.area

    def __str__(self):
        return f'户型是{self.house_type},总面积是{self.house_area},剩余面积是{self.free_area},家具有{self.item_list}'

# 继承
# 在python中，所有类默认继承object类，object类是顶级类或基类；其他子类叫做派生类
class A:
    def __init__(self):
        self.str = '继承'

    def info_print(self):
        print(self.str)

class B(A):
    pass


# 单继承
class Parent(object):
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        # 继承了父类的属性(记住)
        super().__init__(name)
        # Parent.__init__(self,name)
        print('Son1的init结束被调用')


class Grandson(Son1):
    # super()方法
    # def __init__(self, name, age, gender):
    #     print('Grandson的init开始被调用')
    #     self.gender = gender
    #     super().__init__(name, age)
    #     print('Grandson的init结束被调用')
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        self.gender = gender
        # super().__init__(name,age)
        Son1.__init__(self, name, age)
        print('Grandson的init结束被调用')

# 多继承
# 遇到同名方法的时候的调用顺序是什么样子？
# 多继承
# 语法: 子类(父类1，父类2，...)

# 1.多继承：子类有多个父类
class Human:
    def __init__(self, sex):
        self.sex = sex

    def p(self):
        print("这是Human的方法")


class Person:
    def __init__(self, name):
        self.name = name

    def p(self):
        print("这是Person的方法")

    def person(self):
        print("这是我person特有的方法")


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# 多继承的时候只能父类名.__init__方式
class Student(Human, Person):
    def __init__(self, name, sex, grade):
        # 要想调用特定父类的构造器可以使用父类名.__init__方式
        Human.__init__(self, sex)
        Person.__init__(self, name)
        self.grade = grade

    # def p(self):
    #     print('这个是学生独有的p方法')
class Son(Human, Teacher):
    def __init__(self, sex, name, age, fan):
        Human.__init__(self, sex)
        Teacher.__init__(self, name, age)
        self.fan = fan


# ------创建对象 -------------
# stu = Student("tom", "male", 88)
# # 是否继承了父亲的属性并且新增了属性
# print(stu.name, stu.sex, stu.grade)
# stu.p()  # 虽然父类Human和Person都有同名P()方法 ，但是调用的是括号里的第一个父类Human的方法，优先选取，如果第一个没有，去第二个父类去找
# print(Student.__mro__)  # 通过__mro__查看继承顺序

# 私有权限
# 即类独有的属性，其他的类不能调用，方法：定义的属性前加__
class Animal(object):
    def __init__(self):
        self.__age = 100
        self._name = 'yaoyao'  # 一个_是 建议你不要在外面访问，但是你访问了也不会报错

    def run(self):
        print('run')

    def __run(self):
        print('__run')


class Dog(Animal):
    pass

# 异常
'''
try:
except:
'''
# open('text.txt', 'r')   # FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
try:
    open('text.txt', 'r')
except:
    print('如果text.txt不存在，则执行except后面的代码')   #如果text.txt不存在，则执行except后面的代码
# 异常捕获(所有用Exception)
try:
    open('text.txt', 'r')
except Exception as e:  # 不知道错误的类型，可以用Exception这个方法
    print('如果text.txt不存在，则执行except后面的代码')  # 如果text.txt不存在，则执行except后面的代码
    print(e)    # [Errno 2] No such file or directory: 'text.txt'
# 指定错误类型异常捕获,捕获多个指定异常，可以用括号包起来，逗号隔开except (FileNotFoundError, NameError):
try:
    open('text.txt', 'r')
except FileNotFoundError as e:  # 不知道错误的类型，可以用Exception这个方法
    print('如果text.txt不存在，则执行except后面的代码')  # 如果text.txt不存在，则执行except后面的代码
    print(e)    # [Errno 2] No such file or directory: 'text.txt'
# try:  except:   else:     finally:
try:
    open('text.txt', 'r')
except Exception as e:  # 不知道错误的类型，可以用Exception这个方法
    print('如果text.txt不存在，则执行except后面的代码')  # 如果text.txt不存在，则执行except后面的代码
    print(e)
else:
    print('只有在代码不出现异常的情况下才会执行')
finally:
    print('无论代码是否出现异常，finally后面的代码都会被执行')   # 无论代码是否出现异常，finally后面的代码都会被执行





if __name__ == '__main__':
    bed = HouseItem('席梦思', 4)
    chest = HouseItem('衣柜', 2)
    table = HouseItem('餐桌', 1.5)
    print(bed)  # 家具名称是席梦思,面积是4
    myhouse = House('三室一厅', 89)
    print(myhouse)  # 户型是三室一厅,总面积是89,剩余面积是89,家具有[]
    myhouse.add_item(bed)
    myhouse.add_item(chest)
    myhouse.add_item(table)
    print(myhouse)  # 户型是三室一厅,总面积是89,剩余面积是81.5,家具有['席梦思', '衣柜', '餐桌']
    son = B()
    son.info_print()    # 继承
    # 单继承
    gs = Grandson('grandson', 12, '男')
    print('姓名：', gs.name)
    print('年龄：', gs.age)
    print('性别：', gs.gender)
    # 多继承
    son1 = Son("jerry", "female", 18, "打球")
    son1.person()  # 可以调用父类的父类的方法。
    son1.p()  # 子类调用众多父类中同名的方法，按继承的顺序查找。
    print(Son.__mro__)  # 通过__mro__查看继承顺序
    # 私有权限
    a = Animal()
    print(a._name)  # yaoyao
    # print(a.__age)  # 不能被调用
    # a.__run()     # 不能被调用
    # a.run()       # run
    # print(Dog().__age)  # 不能被调用