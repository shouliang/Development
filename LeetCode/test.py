def twoSum(nums, target):
    hash_map = {}
    for i, value in enumerate(nums):
        if target - value in hash_map:
            return hash_map[target - value], i
        hash_map[value] = i


nums, target = [8, 9, 14, 6, 20], 15
twoIndex = twoSum(nums, target)
print(twoIndex)
