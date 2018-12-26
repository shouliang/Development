def merge_sort(alist):
    if not alist: return [];
    merge_sort_helper(alist, 0, len(alist) - 1)


def merge_sort_helper(alist, low, high):
    if low == high: return  # 递归终止条件,low == high,表明指向同一个元素，一个元素本身就是有序的，递归结束，而后开始进行合并

    # 将原数组分成两半，分别进行递归调用
    mid = low + (high - low) // 2
    merge_sort_helper(alist, low, mid)
    merge_sort_helper(alist, mid + 1, high)

    # 合并数组
    merge(alist, low, mid, high)


# 合并两个已经排序的数组到一个数组，仍使其有序
# 通过low,mid,high可以将原数组分成两个有序的数组，然后循环比较，将较小的插入临时数组，最后再复制到原数组，达到使原数组有序的目的
def merge(alist, low, mid, high):
    i, j = low, mid + 1
    tmp = []

    while i < mid and j < high:
        if alist[i] <= alist[j]:
            tmp.append(alist[i])
            i += 1
        else:
            tmp.append(alist[j])
            j += 1

    # 将剩余的全部存入临时数组
    while i <= mid:
        tmp.append(alist[i])
        i += 1
    while j <= high:
        tmp.append(alist[j])
        j += 1

    # 临时数组的数据赋值到原数组
    alist[low:high + 1] = tmp


# 在原数组上进行排序
alist = [3, 5, 6, 7, 8, 1]
merge_sort(alist)
print(alist)

