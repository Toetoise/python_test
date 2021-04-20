'''
工厂模式：创建出的产品都有相同的特点
首先写一些基类(父类)，具有相同的特点，创造出很多具有这些特点的产品，然后独有的特点
继承相同的特点的基础上再拓展就可以用工厂模式
单例模式：有些对象需要具有唯一性，可以用单例模式来实现
'''
class Zhuxi:
    """
    1.不管创建多少对象，内存地址是唯一  __new__魔法方法 给待创建的对象分配内存空间 返回内存地址的引用
    """
    instance = None
    init_flag = False

    def __new__(cls):
        if not cls.instance:
            print("创建第一个实例")
            cls.instance = super().__new__(cls)     # 给待创建的对象分配内存空间
        return cls.instance

    def __init__(self):
        if not self.init_flag:
            print("第一次初始化")
            self.init_flag = True


if __name__ == '__main__':
    a = Zhuxi()
    print(id(a))
    b = Zhuxi()
    print(id(b))
