stu_list = []


def menu_print():
    print('''
    # 1-- 添加学员--存储结构[{'name':,'id':,'tel':}]
    # 2-- 删除学员
    # 3-- 修改学员信息（修改学生电话号码）
    # 4-- 查询学员信息
    # 5-- 显示所有学员信息
    # 6-- 退出系统  
    ''')


def add_stu():
    """
    添加学员,isdigit校验是否只包含数字
    :return:
    """
    stu_name = input('请输入学员姓名:')
    stu_num = input('请输入学员学号:')
    stu_tel = input('请输入学员电话:')
    if stu_num.isdigit() and stu_name and stu_tel.isdigit():
        global stu_list
        for i in stu_list:
            if i['id'] == stu_num:
                print('您输入的学员id已经存在，请重新输入')
                break
        else:
            stu_dic = {'name': stu_name, 'tel': stu_tel, 'id': stu_num}
            stu_list.append(stu_dic)
            print(stu_list)
    else:
        print('您输入的信息格式不正确，请重新输入')


def del_stu():
    """
    删除学员,先判断学号存不存在再执行
    :return:
    """
    stu_id = input('请输入学生id:')
    if stu_id.isdigit():
        global stu_list
        for i in stu_list:
            if i['id'] == stu_id:
                stu_list.remove(i)
                print(f'以删除id为{stu_id}的学生')
        else:
            print('您输入的学生id不存在,请重新输入')
    else:
        print('您输入的信息格式不正确，请重新输入')


def modify_stu():
    """
    修改学员信息，可以修改手机号和姓名
    :return:
    """
    stu_id = input('请输入学生id:')
    if stu_id.isdigit():
        global stu_list
        for i in stu_list:
            if i['id'] == stu_id:
                modify_type = input('请输入想要修改的数据(0-姓名 1-手机号码):')
                if modify_type.isdigit():
                    if modify_type == '0':
                        modify_name = input('请输入新名称:')
                        i['name'] = modify_name
                        print('修改成功')
                        break
                    else:
                        modify_tel = input('请输入新号码:')
                        i['tel'] = modify_tel
                        print('修改成功')
                        break
                else:
                    print('您输入的信息格式不正确，请重新输入')
        else:
            print('您输入的学生id不存在,请重新输入')
    else:
        print('您输入的信息格式不正确，请重新输入')


def query_stu():
    """
    可以通过姓名，手机号码，学号查询学员信息
    :return:
    """
    query_type = input('请输入想要查询的方式(0-姓名 1-手机号码 2-学号):')
    global stu_list
    if query_type.isdigit():
        if query_type == '0':
            query_name = input('请输入想要查询的学员姓名:')
            for i in stu_list:
                if i['name'] == query_name:
                    query_tel = i['tel']
                    query_id = i['id']
                    print(f'您查询的学员是{query_name},学号{query_id},手机号码{query_tel}')
                    break
            else:
                print('您输入的学员不存在，请重新输入')
        elif query_type == '1':
            query_tel = input('请输入想要查询的学员号码:')
            if query_tel.isdigit():
                for i in stu_list:
                    if i['tel'] == query_tel:
                        query_name = i['name']
                        query_id = i['id']
                        print(f'您查询的学员是{query_name},学号{query_id},手机号码{query_tel}')
                        break
                else:
                    print('您输入的学员手机号不存在，请重新输入')
            else:
                print('您输入的信息格式不正确，请重新输入')
        else:
            query_id = input('请输入想要查询的学员学号:')
            if query_id.isdigit():
                for i in stu_list:
                    if i['id'] == query_id:
                        query_name = i['name']
                        query_tel = i['tel']
                        print(f'您查询的学员是{query_name},学号{query_id},手机号码{query_tel}')
                        break
                else:
                    print('您输入的学员不存在，请重新输入')
            else:
                print('您输入的信息格式不正确，请重新输入')
    else:
        print('您输入的信息格式不正确，请重新输入')


def show_all():
    """
    查询所有学员信息
    :return:
    """
    for i in stu_list:
        stu_name = i['name']
        stu_tel = i['tel']
        stu_id = i['id']
        print(f'{stu_name}的学号是{stu_id}手机号码是{stu_tel}')
    print('以上是所有学员信息')


def main():
    """
    主函数,根据需要输入要操作的功能进行判断,同时也是学生管理系统的主入口
    :return:
    """
    while True:
        menu_print()
        user_num = input('请输入您需要操作的功能序号:')
        if user_num == '1':
            add_stu()
        elif user_num == '2':
            del_stu()
        elif user_num == '3':
            modify_stu()
        elif user_num == '4':
            query_stu()
        elif user_num == '5':
            show_all()
        elif user_num == '6':
            break
        else:
            print('您输入的信息有误，请重新输入')


if __name__ == '__main__':
    main()
