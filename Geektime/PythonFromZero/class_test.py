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
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def print_role(self):  # 定义类的一个方法
        print('name is %s,hp is %s' % (self.name, self.hp))


user1 = Player('tom', 100)  # 类的实例化
user2 = Player('jerry', 80)
user1.print_role()
user2.print_role()
