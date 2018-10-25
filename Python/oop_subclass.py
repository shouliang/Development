# coding=utf-8
# 类的继承

# 基类
class SchoolMember:
    '''代表任何学校里的成员'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember: {}'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

# 子类
# 定义子类时需要在类后面跟一个包含基类名称的元组
class Teacher(SchoolMember):
    '''代表一位老师'''

    # 子类中定义了 __init__ 方法，Python不会自动调用基类中的构造函数，需要显式地调用基类中的构造函数
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()