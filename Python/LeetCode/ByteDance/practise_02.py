class Solution:
    def maxAreaOfIsland(self, grid):
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    maxArea = max(maxArea, dfs(grid, i, j, rows, cols))
        return maxArea

    def maxAreaOfIsland_01(self, grid):
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        for i in range(rows):
            for j in range(cols):
                maxArea = max(maxArea, dfs(grid, i, j, cols, rows))
        return maxArea


def dfs(grid, i, j, rows, cols):
    if 0 <= i < rows and 0 <= j < cols and grid[i][j] != 0:
        grid[i][j] = 0
        return 1 + dfs(grid, i-1, j, rows, cols) + dfs(grid, i+1, j, rows, cols) + dfs(grid, i, j-1, rows, cols) + dfs(grid, i, j+1, rows, cols)
    return 0


def dfs_01(grid, i, j, rows, cols):
    if 0 <= i < rows and 0 <= j < cols and grid[i][j] != 0:
        grid[i][j] = 0
    return 1 + dfs_01(grid, i-1, j, rows, cols) + dfs_01(grid, i+1, j, rows, cols) + dfs_01(grid, i, j-1, rows, cols) + dfs_01(grid, i, j+1, rows, cols)

    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    def search_01(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

        def search_02(self, nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + ((high - low) >> 1)
                if nums[mid] == target:
                    return mid
                if nums[mid] >= nums[low]:
                    if nums[low] <= target < nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if nums[mid] < target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            return -1

        def findCircleNum(self, M):
            n = len(M)
            result, visited = 0, [False] * n
            for i in range(n):
                if not visited[i]:
                    self.dfs(M, i, visited)
                    result += 1
            return result

        def dfs(self, M, start, visited):
            visited[start] = True

            for i in range(len(M)):
                if M[start][i] and not visited:
                    self.dfs(M, i, visited)

        def findCircleNum_01(self, M):
            n = len(M)
            result, visited = 0, [False] * n
            for i in range(n):
                if not visited[i]:
                    self.dfs(M, i, visited)
                    result += 1
            return result

        def dfs_01(self, M, start, visited):
            visited[start] = True
            for i in range(len(M)):
                if M[start][i] and not visited:
                    self.dfs(M, i, visited)
                    result += 1
            return result

        def findCircleNum_02(self, M):
            n = len(M)
            result, visited = 0, [False] * len(n)
            for i in range(n):
                if not visited[i]:
                    self.dfs(M, i, visited)
                    result += 1
            return result

        def dfs_02(self, M, start, visited):
            visited[start] = True
            for i in range(len(M)):
                if M[start][i] and not visited[i]:
                    self.dfs_02(M, i, visited)

        def trap(self, height):
            left, right = 0, len(height) - 1
            area = 0
            left_max, right_max = 0, 0
            while left < right:
                left_max = max(left_max, height[left])
                right_max = max(right_max, height[right])
                if left_max < right_max:
                    area += left_max - height[left]
                    left += 1
                else:
                    area += right_max - height[right]
                    right -= 1
            return area

        def trap_01(self, height):
            left, right = 0, len(height) - 1
            area, left_max, right_max = 0, 0, 0,
            while left < right:
                left_max = max(left_max, height[left])
                right_max = max(right_max, height[right])
                if left_max < right:
                    area += left_max - height[left]
                    left += 1
                else:
                    area += right_max - height[right]
                    right -= 1
            return area

        def trap_02(self, height):
            left, right = 0, len(height) - 1
            area, left_max, right_max = 0, 0, 0
            while left < right:
                left_max = max(left_max, height[left])
                right_max = max(right_max, height[right])
                if left_max < right_max:
                    area += left_max - height[left]
                    left += 1
                else:
                    area += right_max - height[right]
                    right -= 1
            return area

        def threeSum(self, nums, target):
            result = []
            nums.sort()
            target = 0
            for i in range(len(nums) - 2):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                left, right = i + 1, len(nums) - 1
                while left < right:
                    diff = (nums[i] + nums[left] + nums[right]) - target
                    if diff < 0:
                        left += 1
                    elif diff > 0:
                        right -= 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
            return result

        def threeSum_01(self, nums):
            result = []
            nums.sort()
            target = 0
            for i in range(len(nums) - 2):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                left, right = i + 1, len(nums) - 1
                while left < right:
                    diff = (nums[i] + nums[left] + nums[right]) - target
                    if diff < 0:
                        left += 1
                    elif diff > 0:
                        right -= 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
            return result

        def threeSum02(self, nums):
            result = []
            nums.sort()
            target = 0
            for i in range(len(nums) - 2):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                left, right = i + 1, len(nums) - 1
                while left < right:
                    diff = (nums[i] + nums[left] + nums[right]) - target
                    if diff < 0:
                        left += 1
                    elif diff > 0:
                        right -= 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            let += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
            return result

            def reverseList(self, head):
                pre, cur = None, head

                while cur:
                    temp = cur.next
                    cur.next = pre

                    pre = cur
                    cur = temp
                return pre

            def reverseList_01(self, head):
                pre, cur = None, head
                while cur:
                    temp = cur.next
                    cur.next = pre

                    pre = cur
                    cur = temp
                return pre

            def reverseList_02(self, head):
                pre, cur = None, head
                while cur:
                    temp = cur.next
                    cur.next = pre

                    pre = cur
                    cur = temp
                return pre

            def mergeKLists(self, lists):
                if not list:
                    return []
                return self.partition(lists, 0, len(list) - 1)

            def partition(self, lists, low, high):
                if low == high:
                    return lists[low]

                mid = low + ((high - low) >> 1)
                left = self.partition(lists, low, mid)
                rihgt = self.partition(lists, mid + 1, high)
                return self.merge(left, right)

            def merge(self, l1, l2):
                if not l1:
                    return l2
                if not l2:
                    return l1
                if l1.val < l2.val:
                    l1.next = self.merge(l1.next, l2)
                    return l1
                else:
                    l2.next = self.merge(l1, l2.next)
                    return l2

            def mergeKLists_01(self, lists):
                if not lists:
                    return []
                return self.partition(lists, 0, len(lists) - 1)

            def partition_01(self, lists, low, high):
                if low == high:
                    return lists[low]
                mid = low + ((high - low) >> 1)
                left = self.partition_01(lists, low, mid)
                right = self.partition_01(lists, mid+1, high)
                return self.merge_01(left, right)

            def merge_01(self, l1, l2):
                if not l1:
                    return l2
                if not l2:
                    return l1
                if l1.val < l2.val:
                    l1.next = self.merge_01(l1.next, l2)
                    return l1
                else:
                    l2.next = self.merge_01(l1, l2.next)
                    return l2

            def mergeKLists_02(self, lists):
                if not lists:
                    return []
                return self.partition_02(lists, 0, len(lists) - 1)

            def partition_02(self, lists, low, high):
                if low == high:
                    return lists[low]
                mid = low + ((high - low) >> 1)
                left = self.partition_02(lists, low, mid)
                right = self.partition_02(lists, mid + 1, high)
                self.merge_02(left, right)

            def merge_02(self, l1, l2):
                if not l1:
                    return l2
                if not l2:
                    return l1
                if l1.val < l2.val:
                    l1.next = self.merge_02(l1.next, l2)
                    return l1
                else:
                    l2.next = self.merge_02(l1, l2.next)
                    return l2

            def maxSubArray(self, nums):
                sub_sum = [0] * len(nums)
                sub_sum[0], max_sum = nums[0], nums[0]

                for i in range(1, len(nums)):
                    if sub_sum[i-1] >= 0:
                        sub_sum[i] = sub_sum[i - 1] + nums[i]
                    else:
                        sub_sum[i] = nums[i]
                    max_sum = max(max_sum, sub_sum)
                return max_sum

            def maxSubArray_01(self, nums):
                sub_sum = [0] * len(nums)
                sub_sum[0], max_sum = nums[0]
                for i in range(1, len(nums)):
                    if sub_sum[i-1] >= 0:
                        sub_sum[i] = sub_sum[i-1] + nums[i]
                    else:
                        sub_sum[i] = nums[i]
                    max_sum = max(max_sum, sub_sum[i])
                return max_sum

            def maxSubArray_02(self, nums):
                sub_sum = [0] * len(nums)
                sub_sum[0], max_sum = nums[0], nums[0]
                for i in range(1, len(nums)):
                    if sub_sum[i - 1] >= 0:
                        sub_sum[i] = sub_sum[i - 1] + nums[i]
                    else:
                        sub_sum[i] = nums[i]
                    max_sum = max(max_sum, sub_sum[i])
                return max_sum
