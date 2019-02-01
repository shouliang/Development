'''
全 O(1) 的数据结构
432. All O`one Data Structure:https://leetcode.com/problems/all-oone-data-structure/
解释：
    实现一个数据结构支持以下操作：

    Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
    Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否者使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。
    GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串""。
    GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。
    挑战：以 O(1) 的时间复杂度实现所有操作。

思路：
    Hash Table + Double linked list
'''


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        pass

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        pass

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        pass

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        pass


