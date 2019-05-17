class Solution:
    def lengthOfLongestSubString(self, s):
        if not s:
            return 0
        longest, i, hash_map = 0, 0, dict()
        for j in range(len(s)):
            if s[j] in hash_map and hash_map[s[j]] + 1 > i:
                i = hash_map[s[j]] + 1
            hash_map[s[j]] = j
            longest = max(longest, j-i+1)
        return longest

    def simplifyPath(self, path):
        if not path:
            return None
        p = path.split("/")
        stack, result = [], ""
        for s in p:
            if s == '.' or len(s) == 0:
                continue
            elif s == '..':
                if len(stack):
                    stack.pop()
            else:
                stack.append(s)

        if len(stack):
            return "/"
        for s in stack:
            result += "/" + s
        return result

    def restoreIpAddress(self, s):
        if len(s) < 4 or len(s) > 12:
            return []
        path, result = [], []
        dfs(s, 0, path, result)
        return result


def dfs(s, start, path, result):
    if len(path) == 4 and start == len(s):
        result.append(".".join(path))
        return
    for i in range(1, 4):
        if start + i <= len(s):
            number = s[start:start+i]
            if str(int(number)) == number and int(number) <= 255:
                path.append(number)
                dfs(s, start+i, path, result)
                path.pop()

        def threeSum(self, nums):
            if not nums:
                return []
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
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
            return result

        def search(self, nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + ((high - low) >> 1)
                if nums[mid] == target:
                    return mid
                if nums[mid] >= nums[low]:
                    if target >= nums[low] and target < nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if target > nums[mid] and target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            return -1

        def trap(self, height):
            left, right = 0, len(height) - 1
            left_max, right_max, areas = 0, 0, 0
            while left < right:
                left_max = max(left_max, height[left])
                right_max = max(right_max, height[right])
                if left_max < right_max:
                    areas += left_max - height[left]
                    left += 1
                else:
                    areas += right_max - height[right]
                    right -= 1
            return areas

        def reverseList(self, head):
            pre, cur = None, head
            while cur:
                temp = cur.next
                cur.next = pre

                pre = cur
                cur = temp
            return pre

        def mergeKLists(self, lists):
            if not lists:
                return []
            return self.partition(lists, 0, len(lists) - 1)

        def partition(self, lists, low, high):
            if low == high:
                return lists[low]
            mid = low + ((high - low) >> 1)
            left = self.partition(lists, low, mid)
            right = self.partition(lists, mid+1, high)
            self.merge(left, right)

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

        def maxSubArray(self, nums):
            if not nums:
                return None
            sub_sum = [0] * len(nums)
            sub_sum[0], max_sum = nums[0], nums[0]
            for i in range(1, len(nums)):
                if sub_sum[i-1] >= 0:
                    sub_sum[i] = sub_sum[i-1] + nums[i]
                else:
                    sub_sum[i] = nums[i]
                max_sum = max(max_sum, sub_sum[i])
            return max_sum

        def findCircleNum(self, M):
            n = len(M)
            visited = [False] * len(n)
            result = 0
            for i in range(len(n)):
                if not visited[i]:
                    self.dfs_friend(M, i, visited)
                    result += 1
            return result

        def dfs_friend(self, M, start, visited):
            visited[start] = True

            for i in range(len(M)):
                if M[start][i] and not visited[i]:
                    self.dfs_f(M, i, visited)

        def maxAreaOfIsland(self, grid):
            maxArea = 0
            rows = len(grid)
            cols = len(grid[0]) if rows else 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j]:
                        maxArea = max(maxArea, self.dfs_island(
                            grid, i, j, rows, cols))
            return maxArea

        def dfs_island(self, grid, i, j, rows, cols):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] != 0:
                grid[i][j] = 0
                return 1 + self.dfs_island(grid, i-1, j, rows, cols) + self.dfs_island(grid, i+1, j, rows, cols)
                + self.dfs_island(grid, i, j-1, rows, cols) + \
                    self.dfs_island(grid, i, j+1, rows, cols)
            return 0
