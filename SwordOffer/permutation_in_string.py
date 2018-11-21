# coding=utf-8
'''
我们知道全排列的含义就是一个序列所有的排序可能性，那么我们现在做这样的一个假设，假设给定的一些序列中第一位都不相同，
那么就可以认定说这些序列一定不是同一个序列，这是一个很显然的问题。
有了上面的这一条结论，我们就可以同理得到如果在第一位相同，可是第二位不同，那么在这些序列中也一定都不是同一个序列，这是由上一条结论可以获得的。
那么，这个问题可以这样来看。我们获得了在第一个位置上的所有情况之后，抽去序列T中的第一个位置，那么对于剩下的序列可以看成是一个全新的序列T1，
序列T1可以认为是与之前的序列毫无关联了。同样的，我们可以对这个T1进行与T相同的操作，直到T中只一个元素为止。这样我们就获得了所有的可能性。
所以很显然，这是一个递归算法。

这里出现了好多的重复。重复的原因当然是因为我们列举了所有位置上的可能性，而没有太多地关注其真实的数值。
现在，我们这样来思考一下，如果有一个序列T = {a1, a2, a3, …, ai, … , aj, … , an}。
其中，a[i] = a[j]。那么是不是就可以说，在a[i]上，只要进行一次交换就可以了，a[j]可以直接忽略不计了。
好了，基于这样一个思路，我们对程序进行一些改进。我们每一次交换递归之前对元素进行检查，
如果这个元素在后面还存在数值相同的元素，那么我们就可以跳过进行下一次循环递归
（当然你也可以反着来检查某个元素之前是不是相同的元素）。

'''


class Solution:
    def __init__(self):
        self.resultArray = []

    def Permutation(self, ss):
        if not ss:
            return []
        self.PermutationCore(list(ss), 0, len(list(ss)))
        return self.resultArray

    # 判断是否有重复的字符串
    def swapAccepted(self, arr, begin, end):
        for i in range(begin, end):
            if arr[i] == arr[end]:
                return False
        return True

    def PermutationCore(self, arr, begin, end):
        if end - 1 == begin:
            self.resultArray.append(''.join(arr))
            return
        else:
            for i in range(begin, end):  # 把第一个元素分别与后面的元素进行交换，递归的调用其子数组进行排序
                if not self.swapAccepted(arr, begin, i):  # 有重复的字符串则不进行交换，直接跳过
                    continue
                else:
                    temp = arr[begin]
                    arr[begin] = arr[i]
                    arr[i] = temp

                    self.PermutationCore(arr, begin + 1, end)

                    temp = arr[begin]  # 用于对之前交换过的数据进行还原
                    arr[begin] = arr[i]
                    arr[i] = temp


s = Solution()

ss = 'abc'
print(s.Permutation(ss))

# ss = "aa"
# print(s.Permutation(ss))
