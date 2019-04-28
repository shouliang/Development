def mergeSort(nums):
    if not nums:
        return []
    helper(nums, 0, len(nums) - 1)


def helper(num, low, high):
    if low == high:
        return
    mid = low + ((high - low) >> 1)
    helper(nums, low, mid)
    helper(nums, mid+1, high)
    merge(nums, low, mid, high)


def merge(nums, low, mid, high):
    i, j = low, mid + 1
    temp = []
    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= high:
        temp.append(nums[j])
        j += 1

    nums[low:high+1] = temp


nums = [5, 4, 2, 3, 1, 9, 7, 8, 6]
mergeSort(nums)
print(nums)
