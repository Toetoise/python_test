myCatName = "黑猫警长"
age = 6
weight = 17.365
print('我的小猫的名字叫%s，它的年龄是%06d，它的体重是%.1f' % (myCatName, age, weight))
print(f'我的小猫的名字叫{myCatName}，它的年龄是{age}，它的体重是{weight}')
print('我的小猫的名字叫{}，它的年龄是{}，它的体重是{}'.format(myCatName, age, weight))

num = 7     # int类型不可以被迭代not iterable
str1 = 'wwww'
t1 = (1, 2, 3, 4, 5)
dic1 = {'name': '黑猫警长', 'age': '8'}     # 只保留key
# print(list(num))
print(list(str1))
print(list(t1))
print(list(dic1))

result = eval('35+22')      # eval() 可以把字符串表达的数学式进行计算
print(result)

li = [1, 2, 4, 4, 'cat', 'dog', 'cat']
new_set = set(li)     # set()把转换成集合且去重了
print(new_set)
new_li = list(new_set)
print(new_li)       # 达到去重的效果

a = 1
b = 2
c = 3
print(a, end='')        # end结束符\n是换行,不要\n是不换行
print(b, end='\n')
print(c)

print("""
你好，
我是何同学
""")        # 三单引号或三双引号可以把换行的字符串完整的打印出来

name = "大家好我是何同学"
print(name[3])
print(name[-2])     # 可以逆向取值
print(name[3:7:1])      # 切片取值，[起始:结束:步长],不包括结束位置的字符  我是何同
print(name[-7:-1:1])        # 逆向切片取值，不包括起始位置的字符  家好我是何同
print(name[::])    # 包含起始和结束位置
print(name[::-1])   # 倒置
print(name[-2:4:-1])    # 同何

str1 = '1 and 2 and 3'
print(str1.find('and'))     # 返回的是查找的字符串在字符串中起始位置 2
print(str1.find('and', 3, 12))      # 返回的是在指定区间内的字符串的位置 8
print(str1.find('4'))       # 没有该字符串返回-1
print(str1.rfind('and'))       # 从右往左找
print(str1.index('and'))       # 与find相同
print(str1.count('and'))       # 子字符串出现的次数 2

name = "大家好我是何同学"
print(name.replace('家', '家家', 1))       # replace() [被替换的字符串, 替换的, 次数] 不输入次数默认是全部 大家家好我是何同学
print(str1.replace('and', 'or', 3))     # 次数大于默认子字符串数量时，取全部    1 or 2 or 3
print(name.split('好'))      # split('字符串中的内容', 次数) 以内容左右切割字符串为列表   ['大家', '我是何同学']
print(str1.split(' '))      # ['1', 'and', '2', 'and', '3']

new_name = name.split('好')
print('好'.join(new_name))       # 将列表加入到列表中   ''.join()     大家好我是何同学

# capitalize()    字符串的第一个字符大写
# title()     字符串中每一个单词首字母大写
# lower()     将字符串中大写转换成小写
# upper()     将所有小写转换成大写
# lstrip()    删除字符串左侧的空白字符
# rstrip()    删除字符串右侧的空白字符
# strip()     删除字符串左右两侧的空白字符

str1 = 'start'
print(str1.ljust(10, '*'))      # ljust()左对齐,[长度，字符]   start***** 不够的长度以字符填充
print(str1.rjust(10, '$'))      # rjust()右对齐    $$$$$start
print(str1.center(10, '='))     # center()中心对齐      ==start===
