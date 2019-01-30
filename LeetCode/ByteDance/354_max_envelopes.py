''' 
俄罗斯套娃
354. Russian Doll Envelopes:https://leetcode.com/problems/russian-doll-envelopes/
解释:
    给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
    这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

    请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

    说明:
    不允许旋转信封。

    示例:
    输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    输出: 3 
    解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

    思路：
    俄罗斯套娃信封问题的本质是一个二维版的 LIS（最长递增子列）,
    参见：leetcode 300. Longest Increasing Subsequence:https://leetcode.com/problems/longest-increasing-subsequence/
    
    思路1：动态规划：O(n^2),首先按照宽度升序，而后就转换为按高度求最长递增子序列的问题：
                   dp[i] 表示以第i个元素为结尾的增长序列的长度，
                   则递归式为：dp[i]= max(dp[i], dp[j] + 1) 其中 j 0..i-1 && nums[i] > nums[j]

    思路2：Θ(nlgn)的方案，二分查找
        以输入envelopes其中的一个维度进行排序，对另外一个维度求解LIS即可。
        1. 对输入的envelopes进行排序：首先比较宽度，宽度小的在前；宽度相同时，
        高度大的在前（这样处理可以避免相同宽度的信封被重复统计）
        2. 利用二分查找维护一个递增队列，以高度作为比较条件。
'''


class Solution(object):
    def _maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        result = 1
        nums = sorted(envelopes, key=lambda x: x)  # 首先按宽度width升序
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i][0] > nums[j][0] and nums[i][1] > nums[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
         # sorted不改变原数组，返回一个新的数组
        tails = []
        envs = sorted(envelopes, key=lambda x: (x[0], -x[1]))  # 排序：按宽度升序、高度降序
        for (w, h) in envs:
            if len(tails) == 0 or tails[-1] < h:
                tails.append(h)
            else:
                low, high = 0, len(tails) - 1
                while low <= high:
                    mid = low + ((high - low) >> 1)
                    if tails[mid] >= h:
                        high = mid - 1
                    else:
                        low = mid + 1
                tails[low] = h
        return len(tails)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
s = Solution()
max_len = s.maxEnvelopes(envelopes)
print(max_len)
