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
'''

# TODO: 未做完，暂时不想做了
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = dict()

        self.max_key = None
        self.max_value = 0
        self.min_key = None
        self.min_value = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if not self.hash_map:
            self.hash_map[key] = 1
            self.max_key = key
            self.max_value = 1
            self.min_key = key
            self.min_value = 1
        else:
            if key in self.hash_map:
                self.hash_map[key] += 1
                if(self.hash_map[key] > self.max_value):
                    self.max_key = key
                    self.max_value = self.hash_map[key]
                if self.hash_map[key] < self.min_value:
                    self.min_key = key
                    self.min_value = self.hash_map[key]
            self.hash_map[key] = 1

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.hash_map:
            if self.hash_map[key] == 1:
                self.hash_map.pop(key)
            else:
                self.hash_map[key] -= 1
                if(self.hash_map[key] > self.max_value):
                    self.max_key = key
                    self.max_value = self.hash_map[key]
                if self.hash_map[key] < self.min_value:
                    self.min_key = key
                    self.min_value = self.hash_map[key]

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.max_key or ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.min_key or ''
