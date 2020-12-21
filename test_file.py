f = open("C:\\Users\\Tortoise\\Desktop\\111.txt", encoding='utf-8')
# 返回一个文件对象,读取中文内容encoding声明一下
line = f.readline()             # 调用文件的 readline()方法
while line:
    # print line,                 # 在 Python 2中，后面跟 ',' 将忽略换行符
    print(line, end='')       # 在 Python 3中使用
    line = f.readline()
f.close()