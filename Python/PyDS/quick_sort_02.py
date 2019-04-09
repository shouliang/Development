# coding=utf-8
# 有辅助数组的做法
def quick_sort(array):
    if not array:
        return []

    less,greater = [],[]
    pivot_value = array.pop()

    for value in array:
        if value < pivot_value:
            less.append(value)
        else:
            greater.append(value)

    return quick_sort(less) + [pivot_value] + quick_sort(greater)

arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
print(quick_sort(arr))

