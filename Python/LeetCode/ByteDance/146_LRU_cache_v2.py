'''
LRU缓存机制
146. LRU Cache:https://leetcode.com/problems/lru-cache/
解释：
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。

思路1：    
单链表：我们维护一个有序单链表，越靠近链表尾部的结点是越早之前访问的。当有一个新的数据被访问时，我们从链表头开始顺序遍历链表。
1. 如果此数据之前已经被缓存在链表中了，我们遍历得到这个数据对应的结点，并将其从原来的位置删除，然后再插入到链表的头部。
2. 如果此数据没有在缓存链表中，又可以分为两种情况：
    如果此时缓存未满，则将此结点直接插入到链表的头部；
    如果此时缓存已满，则链表尾结点删除，将新的数据结点插入链表的头部。


思路2：
双链表+哈希表
分析每个操作的耗费：
get(key)时
    判断key是否在哈希表中，使用hashtable，复杂度为O(1)
    获取相应位置链表的头指针head，并设定其指向key值对应节点（确保最新访问的放在链表头部）
    如果key不在链表中，则将key插入到链表头部，此处调用set(key)
    如果key在链表中，则将key节点移动到链表头部，复杂度为O(1)
set(key)时
    如果该链表长度不超过设定值，则直接插入到头部。
    如果链表长度超过设定值，则删除最后一个元素，再插入key到链表第一个节点。
参考:https://qiankunli.github.io/2014/10/21/lru.html
'''


class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


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
