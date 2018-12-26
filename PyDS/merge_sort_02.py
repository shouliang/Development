def merge_sort(alist):
    if not alist: return [];  # 错误处理
    if len(alist) == 1: return alist;  # 递归终止条件

    mid = (len(alist)) // 2  # 数组一分为二
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    left = merge_sort(left)  # 嵌套递归调用左右部分
    right = merge_sort(right)
    return merge(left, right)  # 合并左右有序的数组


def merge(left, right):
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged  # 合并后的数组是一个新的数组


alist = [6, 4, 5, 1, 3]
# 返回排序好的新数组
sorted = merge_sort(alist)
print(sorted)
