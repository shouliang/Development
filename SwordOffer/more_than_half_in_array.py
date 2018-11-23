class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return None

        result = numbers[0]
        times = 0
        for value in numbers:
            if times == 0:
                result = value
                times = 1
            if value == result:
                times += 1
            else:
                times -= 1

        return result

numbers = [1,2,3,2,2,2,5,4,2]

s = Solution()
result = s.MoreThanHalfNum_Solution(numbers)
print(result)