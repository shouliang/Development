# 可变参数，通过使用星号来实现
# *param，从此处开始直到结束的所有位置参数都将被收集到一个称为"param"的元组中
# **param,从此处开始直到结束的所有关键字参数都会被收集到一个名为"param"的字典中

def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inger=1560))
