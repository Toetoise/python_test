# 正则表达式
# 1.需求：匹配出一个字符穿第一个字母为大写字符，后面都是小写字母并且这些小写字母可有可无
import re
# 正则表达式
print(re.match(r'[A-Z][a-z]*', 'Maaaa33').group())      # Maaaa

# 2.需求:匹配出8到20位的密码，可以是大小写英文字母、数字、下划线
# {8,20}  \w = [a-zA-Z0-9_]
result = re.match(r'\w{8,20}', 'BaaaaCaoooo_7o').group()
result1 = re.match(r'[a-zA-Z0-9_]{8,20}', 'BaaaaCaoooo_7o').group()
print(result)       # BaaaaCaoooo_7o
print(result1)      # BaaaaCaoooo_7o

# 3.需求：匹配以数字开头中间内容不管以数字结尾   \d
result = re.match(r'^\d.*\d$', '1ui=6').group()
print(result)       # 1ui=6

# 4.需求：第一个字符除了aeiou的字符都匹配
print(re.match(r'^[^aeiou].*', 't8_8K2').group())   # t8_8K2

# 5.需求：匹配出163、126、qq等邮箱
# {4,20}一般邮箱的位数
# (***|***|***)表示一组数据，这组数据具有相同的意义，｜表示或者的意思
print(re.match(r'[a-zA-Z0-9_]{4,20}@(163|126|qq|foxmail)\.com$', 'hello2_A6@126.com').group())  # hello2_A6@126.com

# 6.需求：匹配出line = "Cats are smarter than dogs" 里面的Cats和smarter
# findall()扫描整个字符串，找出所有符合条件的字符串,其返回值是一个列表，没有group属性
line = "Cats are smarter than dogs"
print(re.findall(r'(Cats|smarter)', line))    # ['Cats', 'smarter']
print(re.findall(r'(.*) are (.*) than dogs', line))     # [('Cats', 'smarter')]

# 7.需求：在列表中["apple", "banana", "orange", "pear"],匹配apple和pear
line = ["apple", "banana", "orange", "pear"]
for i in line:
    result = re.match(r'apple|pear', i)
    if result:
        print(result.group())
    else:
        pass        # apple     pear

# 8.需求：匹配出<html>hh</html> 分组匹配 r 的可以不用手动的转义\
print(re.match(r'<[a-z1-6]+>.*</[a-z1-6]+>', '<p1>hasidha1_1</p1>').group())    # <p1>hasidha1_1</p1>
# 同样的规则也可以应用，\1,\2,\3 来引用
print(re.match(r'<([a-z1-6]+)>.*</\1>', '<p1>hasidha1_1</p1>').group())    # <p1>hasidha1_1</p1>
# 也可以对规则进行命名，再次引用用名字调用 (?P<名字>) (?P=名字)
print(re.match(r'<(?P<name>[a-z1-6]+)>.*</(?P=name)>', '<p1>helloworld</p1>').group())    # <p1>helloworld</p1>


