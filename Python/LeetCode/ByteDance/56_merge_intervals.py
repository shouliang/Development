'''
合并区间
56. Merge Intervals:https://leetcode.com/problems/merge-intervals/
解释：
    Given a collection of intervals, merge all overlapping intervals.

    Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    Example 2:

    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # 先按照start进行排序
        intervals.sort(key=lambda x: x.start)

        result = []
        for interval in intervals:
            # 结果集为空或者结果集的最后一个元素的end < 当前元素的start ,添加当前元素
            if not result or result[-1].end < interval.start:
                result.append(interval)
            else:
                # 否则进行合并，改变结果集的最后一个元素的end，使其为最后一个元素本身的end和当前元素的end中的较大值
                result[-1].end = max(result[-1].end, interval.end)

        return result


intervlas = [
    Interval(1, 3),
    Interval(2, 6),
    Interval(8, 10),
    Interval(15, 18)
]

s = Solution()
ret = s.merge(intervlas)
for i in ret:
    print(i.start, i.end)
