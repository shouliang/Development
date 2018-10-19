# __init_是类的对象呗实例化时立即运行，可以理解为其他语言中的构造函数，第一个参数为self
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

# 类名后面跟上一对括号来创建一个对象
p = Person('Swaroop')
p.say_hi()

# 也可以写作以下方式
Person('Swaroop').say_hi()