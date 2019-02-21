# --------- 面向函数编程 ---------
user1 = {
    'name': 'tom',
    'hp': 100
}
user2 = {
    'name': 'jerry',
    'hp': 80
}


def print_role(rolename):
    print('name is %s,hp is %s' % (rolename['name'], rolename['hp']))


print_role(user1)
print_role(user2)


#  --------- 面向对象编程  ---------

class Player():  # 定义类
    def __init__(self, name, hp, occu):
        self.__name = name
        self.hp = hp
        self.occu = occu

    def print_role(self):  # 定义类的一个方法
        print('name is %s,hp is %s occu is %s' % (self.__name, self.hp, self.occu))

    def updateName(self, newname):
        self.__name = newname


class Monster():
    '定义怪物类'
    pass


user1 = Player('tom', 100, 'war')  # 类的实例化
user2 = Player('jerry', 80, 'master')
user1.print_role()
user2.print_role()

user1.updateName('wilson')
user1.print_role()

# 也可以通过构造函数来实现，但是如果将属性名前加上双下滑杠__则不能实现直接修改
user1.name = 'aaa'
user1.print_role()
