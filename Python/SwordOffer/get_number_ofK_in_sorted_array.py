'''
题目:
统计一个数字在排序数组中出现的次数. 例如输入排序数组{1,2,3,3,3,3,4,5},由于3在这个数中出现了4次,输出4.

思路:

如何利用二分查找找到第一个k? 二分查找算法总是先拿数组中间的数组和k作比较.
如果中间数字比k大,那么k只可能出现数组的前半段,下一轮只在数组的前半段查找就可以了.
如果中间数字比k小,那么k只可能出现数组的后半段,下一轮只在数组的后半段查找就可以了.
如果中间数组和k相等,先判断这个数字是不是第一个k.
如果位于中间数字前面的一个数字不是k,那么此时中间的数字刚好就是第一个k.
如果中间数字的前面一个数字也是k,也就是说第一个k肯定在数组的前半段,下一轮仍然需要在数组的前半段查找.

基于同样的思路可以在排序数组中找到最后一个k.
如果中间数字比k大,那么k只能出现在数组的前半段.
如果中间数字比k小,那么k只能出现在数组的后半段.
如果中间数子和k相等,需要判断这个数字是不是最后一个k.
如果位于中间数字后面一个数字不是k,那么此时中间的数字刚好就是最后一个k.
如果中间数字的后面一个数字也是k,也就是说第一个k肯定在数组的后半段,下一轮仍然需要在数组的后半段查找.
'''


class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return -1
        first_index = GetFirstK(data, k)
        last_index = GetLastK(data, k)

        if first_index > -1 and last_index > -1:
            return last_index - first_index + 1
        return -1


# 二分查找的变形
# 寻找第一个k的索引
def GetFirstK(numbers, key):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = low + ((high - low) >> 1)
        if numbers[middle] == key:
            if (middle > 0 and numbers[middle - 1] != key) or middle == 0:
                return middle
            else:
                high = middle - 1  # 在前半部分继续寻找key, 直到numbers[middle - 1] == key或者寻找第一个即middle = 0
        if numbers[middle] > key:
            high = middle - 1
        if numbers[middle] < key:
            low = middle + 1

    return -1


# 寻找最后一个k的索引
def GetLastK(numbers, key):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = low + ((high - low) >> 1)
        if numbers[middle] == key:
            if middle == high or (middle > 0 and numbers[middle + 1] != key):
                return middle
            else:
                low = middle + 1
        if numbers[middle] > key:
            high = middle - 1
        if numbers[middle] < key:
            low = middle + 1

    return -1


s = Solution()
array = [1, 3, 3, 3, 3, 4, 5]
key = 2

count = s.GetNumberOfK(array, key)
print(count)
