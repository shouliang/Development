def bubbleSort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j+1)

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

nums = [4, 5, 9, 2, 3, 1, 7, 6, 8]
bubbleSort(nums)
print(nums)


def insertionSort(nums):
    n = len(nums)
    for i in range(1,n):
        insertValue = nums[i]
        j = i - 1 
        while j >=0 and nums[j] > insertValue:
            nums[j + 1] = nums[j] 
            j = j - 1
        nums[j + 1] = insertValue

nums1 = [4, 5, 9, 2, 3, 1, 7, 6, 8]
insertionSort(nums1)
print(nums1)

def selectionSort(nums):
    n = len(nums)
    for i in range(n - 1):
        minIndex = i
        for j in range(i+1,n):
            if nums[j] < nums[minIndex]:
                minIndex = j
        
        if i != minIndex:
            swap(nums,i,minIndex)


nums2 = [4, 5, 9, 2, 3, 1, 7, 6, 8]
insertionSort(nums2)
print(nums2)