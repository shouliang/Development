# coding=utf-8
# 类变量和对象变量
class Robot:
    """表示有一个带有名字的机器人"""

    # 一个类变量，用来计数机器人的数量
    # population属于Robot类，因此它是一个类变量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name  # name 为对象变量，因为通过self来分配
        print("(Initializing {})".format(self.name))

        # 当有人被创建，机器人数量增加1
        # 通过类名.变量来直接引用类变量
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候"""
        print('Greetings, my masters call me {}'.format(self.name))

    # 用装饰器来标识为类方法
    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here.\n')

print("Robots have finished their work.So let's destroy them.")
droid1.die()
droid2.die()

# 通过类名.方法名来执行类方法
Robot.how_many()

print('doc example')
print(Robot.__doc__)
print(Robot.say_hi.__doc__)
