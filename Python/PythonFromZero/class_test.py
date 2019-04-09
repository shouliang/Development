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

    def __init__(self, hp=100):
        self.hp = hp  # 生命值

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物父类')


# 子类
class Animals(Monster):
    '普通怪物'

    # def __init__(self, hp=10):
    #     self.hp = hp
    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    'Boss类怪物'

    def __init__(self, hp=100):
        super().__init__(hp)

    # 会覆盖掉父类的同名方法
    def whoami(self):
        print('我是怪物我怕谁')


# user1 = Player('tom', 100, 'war')  # 类的实例化
# user2 = Player('jerry', 80, 'master')
# user1.print_role()
# user2.print_role()
#
# user1.updateName('wilson')
# user1.print_role()
#
# # 也可以通过构造函数来实现，但是如果将属性名前加上双下滑杠__则不能实现直接修改
# user1.name = 'aaa'
# user1.print_role()

a1 = Monster(200)
print(a1.hp)
a1.run()

a2 = Animals(1)
print(a2.hp)
a2.run()

a3 = Boss(800)
a3.whoami()

# type 类型
print('a1的类型 %s' % (type(a1)))
print('a2的类型 %s' % (type(a2)))
print('a3的类型 %s' % (type(a3)))

# 判断是否是子类
print(isinstance(a2, Monster))

# 基类是 object
print(isinstance(123, object))
print(isinstance('abc', object))
