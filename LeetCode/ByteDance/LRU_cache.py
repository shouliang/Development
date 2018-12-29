import collections

class LRUCache:

    def __init__(self, capacity):
        # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
        # OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        val = self.dic.pop(key)
        self.dic[key] = val      # 每次重新赋值，让其成为最新的一个
        return val

    # key已经存在,则pop出，重新赋值；
    # key不存在，若还有剩余空间则剩余空间减1，无剩余空间则淘汰最后一个，也需要重新赋值key,让其成为最新的一个;
    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)

        self.dic[key] = value    # 每次重新赋值，让你成为最新的一个

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # 返回  1
cache.put(3, 3)    # 该操作会使得密钥 2 作废
cache.get(2)       # 返回 -1 (未找到)
cache.put(4, 4)    # 该操作会使得密钥 1 作废
cache.get(1)       # 返回 -1 (未找到)
cache.get(3)       # 返回  3
cache.get(4)       # 返回  4