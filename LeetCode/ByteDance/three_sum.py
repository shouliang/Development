'''
三数之和：

思路：
这道题让我们求三数之和，比之前那道Two Sum要复杂一些，博主考虑过先fix一个数，然后另外两个数使用Two Sum那种HashMap的解法，但是会有重复结果出现，
就算使用set来去除重复也不行，会TLE，看来此题并不是考我们Two Sum的解法。
那么我们来分析一下这道题的特点，要我们找出三个数且和为0，那么除了三个数全是0的情况之外，肯定会有负数和正数，
我们还是要先fix一个数，然后去找另外两个数，我们只要找到两个数且和为第一个fix数的相反数就行了，既然另外两个数不能使用Two Sum的那种解法来找，
如果能更有效的定位呢？我们肯定不希望遍历所有两个数的组合吧，所以如果数组是有序的，那么我们就可以用双指针以线性时间复杂度来遍历所有满足题意的两个数组合。
我们对原数组进行排序，然后开始遍历排序后的数组，这里注意不是遍历到最后一个停止，而是到倒数第三个就可以了。
这里我们可以先做个剪枝优化，就是当遍历到正数的时候就break，为啥呢，因为我们的数组现在是有序的了，
如果第一个要fix的数就是正数了，那么后面的数字就都是正数，就永远不会出现和为0的情况了。
然后我们还要加上重复就跳过的处理，处理方法是从第二个数开始，如果和前面的数字相等，就跳过，
因为我们不想把相同的数字fix两次。对于遍历到的数，用0减去这个fix的数得到一个target，然后只需要再之后找到两个数之和等于target即可。
我们用两个指针分别指向fix数字之后开始的数组首尾两个数，如果两个数和正好为target，则将这两个数和fix的数一起存入结果中。
然后就是跳过重复数字的步骤了，两个指针都需要检测重复数字。如果两数之和小于target，则我们将左边那个指针i右移一位，使得指向的数字增大一些。
同理，如果两数之和大于target，则我们将右边那个指针j左移一位，使得指向的数字减小一些

简单版：先排序，固定第1个，找出第2个、第3个，通过双指针的方式，逐渐缩小范围，中间涉及到相邻元素判重的问题等细节

'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()   # 对原数组进行排序
        target = 0    # target设置为0，因为是此题要求，实际上可以改成任何数字
        for i in range(len(nums) - 2):             # 第一层循环遍历到倒数第三个即可， 第一层循环固定第1个数字
            if i > 0 and nums[i] == nums[i - 1]:   # 相邻的两个相等则直接跳过,防止出现重复
                continue
            left, right = i + 1, len(nums) - 1     # 注意此处left是从i+1开始的
            while left < right:                    # 双指针，逐渐缩小范围，双指针确定第2个、第3个数
                diff = (nums[i] + nums[left] + nums[right]) - target
                if diff < 0:
                    left += 1
                elif diff > 0:
                    right -= 1
                elif diff == 0:
                    res.append((nums[i], nums[left], nums[right]))        # 符合条件，加入结果集
                    while left < right and nums[left] == nums[left + 1]:  # 相邻的元素相等的则直接跳过
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # diff == 0时，left大一点，right小一点，还是有可能等于target的
                    left += 1
                    right -= 1

        return res


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
res = s.threeSum(nums)
print(res)
