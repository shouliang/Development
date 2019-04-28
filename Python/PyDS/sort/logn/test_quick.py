def quickSort(nums):
    if not nums: return []
    helper(nums,0,len(nums) - 1)

def helper(nums,low,high):
    if low>=high: return 
    pivot = partition(nums,low,high)
    helper(nums,low,pivot- 1)
    helper(nums,pivot+1,high)

def partition(nums,low,high):
    pivotValue = nums[high]
    i = low 
    for j in range(low,high):
        if nums[j] < pivotValue:
            swap(nums,i,j)
            i = i + 1
    swap(nums,i,high)
    return i 

def swap(nums,i,j):
    nums[i],nums[j] = nums[j],nums[i]

nums = [5, 4, 2, 3, 1, 9, 7, 8, 6]
quickSort(nums)
print(nums)
