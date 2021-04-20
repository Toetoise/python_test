from student import Student
# import os


class StudentManager:
    def __init__(self):
        """
        {学生id：学生的对象，学生ID：学生的对象}
        """
        self.students_dict = {}

    @staticmethod
    def menu():
        print('''
            # 1-- 添加学员
            # 2-- 删除学员
            # 3-- 修改学员信息
            # 4-- 查询学员信息
            # 5-- 显示所有学员信息
            # 6-- 退出系统  
            ''')

    def startup(self):
        # 读取文件中的学员信息
        self.load_to_file('data.txt')
        while True:
            self.menu()
            user_num = input('请输入您需要操作的功能序号:')
            if user_num == '1':
                self.add_stu()
            elif user_num == '2':
                self.del_stu()
            elif user_num == '3':
                self.modify_stu()
            elif user_num == '4':
                self.query_stu()
            elif user_num == '5':
                self.show_all()
            elif user_num == '6':
                # 保存学员信息
                self.save_to_file('data.txt')
                break
            else:
                print('您输入的信息有误，请重新输入')

    def add_stu(self):
        name = input('请输入学员姓名:')
        id = input('请输入学员学号:')
        score = input('请输入学员分数:')
        if id.isdigit() and score.isdigit() and name:
            if id in self.students_dict.keys():
                print('学生已经存在')
                return
            else:
                student = Student(id, name, score)
                self.students_dict[id] = student
                print('添加学生'+id+'成功')
        else:
            print('您输入的信息格式不正确，请重新输入')

    def del_stu(self):
        id = input('请输入学员学号:')
        if id in self.students_dict.keys():
            del self.students_dict[id]
            print('删除成功')
        else:
            print('没有这个学生')
            return

    def modify_stu(self):
        id = input('请输入学员学号:')
        if id in self.students_dict.keys():
            modify_type = input('请输入想要修改的数据(0-姓名 1-分数):')
            student = self.students_dict[id]
            if modify_type.isdigit():
                if modify_type == '0':
                    modify_name = input('请输入新名称:')
                    student.name = modify_name
                    print('修改成功')
                else:
                    modify_score = input('请输入分数:')
                    student.score = modify_score
                    print('修改成功')
            else:
                print('您输入的信息格式不正确，请重新输入')

    def query_stu(self):
        query_type = input('请输入想要查询的方式(0-姓名 1-学号):')
        if query_type.isdigit():
            if query_type == '0':
                query_name = input('请输入想要查询的学员姓名:')
                for student in self.students_dict.values():
                    if student.name == query_name:
                        print('学号'.ljust(10) + '姓名'.ljust(12) + '分数'.rjust(10))
                        print('-' * 40)
                        id = student.id
                        name = student.name
                        score = student.score
                        print(id.ljust(11) + name.ljust(12) + score.rjust(13))
                        print('-' * 40)
                        break
                else:
                    print('您输入的学员不存在，请重新输入')
                    return
            else:
                query_id = input('请输入想要查询的学员学号:')
                if query_id in self.students_dict.keys():
                    print('学号'.ljust(10) + '姓名'.ljust(12) + '分数'.rjust(10))
                    print('-' * 40)
                    student = self.students_dict[query_id]
                    id = student.id
                    name = student.name
                    score = student.score
                    print(id.ljust(11) + name.ljust(12) + score.rjust(13))
                    print('-' * 40)
                else:
                    print('您输入的学员不存在，请重新输入')
                    return
        else:
            print('您输入的信息格式不正确，请重新输入')

    def show_all(self):
        if len(self.students_dict) == 0:
            print('系统中还没有学员的信息\n')
        else:
            print('学号'.ljust(10)+'姓名'.ljust(12)+'分数'.rjust(10))
            print('-'*40)
            for student in self.students_dict.values():
                id = student.id
                name = student.name
                score = student.score
                print(id.ljust(11) + name.ljust(12) + score.rjust(13))
                print('-'*40)

    def load_to_file(self, file):
        f = open(file, 'r', encoding='UTF-8')
        for line in f.readlines():
            # 因为存储时有换行符，提取前n-1行，每行以,分割，生成组
            student_info = line[:-1].split(',')
            id = student_info[0]
            name = student_info[1]
            score = student_info[2]
            student = Student(id, name, score)
            self.students_dict[id] = student
        f.close()

    def save_to_file(self, file):
        f = open(file, 'w', encoding='UTF-8')
        for student in self.students_dict.values():
            f.write(str(student)+'\n')
        f.close()

# if __name__ == '__main__':
#     s = StudentManager()
#     s.startup()
