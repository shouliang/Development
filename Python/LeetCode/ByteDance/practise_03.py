class Solution:
    def lengthOfLongestSubString(self, s):
        if not s:
            return 0
        longest, i, hash_map = 0, 0, dict()
        for j in range(len(s)):
            if s[j] in hash_map and hash_map[s[j]] + 1 > i:
                i = hash_map[s[j]] + 1
            hash_map[s[j]] = j
            longest = max(longest, j - i + 1)
        return longest

    def simplifyPath(self, path):
        if not path:
            return None
        p = path.split("/")
        stack, result = [], ""
        for s in p:
            if s == "." or len(s) == 0:
                continue
            elif s == "..":
                if len(stack):
                    stack.pop()
            else:
                stack.append(s)

        if len(stack) == 0:
            return "/"
        for s in stack:
            result += "/" + s
        return result

    def restoreIpAddress(self, s):
        if len(s) < 4 or len(s) > 12:
            return []
        path, result = [], []
        self.dfs(s, 0, path, result)
        return result

    def dfs(self, s, start, path, result):
        if len(path) == 4 and start == len(s):
            result.append(".".join(path))
            return
        for i in range(1, 4):
            if start + i <= len(s):
                number = s[start:start+i]
                if str(int(number)) == number and int(number) <= 255:
                    path.append(number)
                    self.dfs(s, start + i, path, result)
                    path.pop()

    def threeSum(self, nums):
        res = []
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
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

        def maxAreaOfIsland(self, grid):
            maxArea = 0
            rows = len(grid)
            cols = grid[0] if rows else 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j]:
                        maxArea = max(maxArea, self.dfs_(
                            grid, i, j, rows, cols))

            return maxArea

        def dfs_(self, grid, i, j, rows, cols):
            if i >= 0 and i < rows and j >= 0 and j < cols and grid[i][j] != 0:
                grid[i][j] = 0
            return 1 + self.dfs_(grid, i-1, j, rows, cols) + self.dfs_(grid, i+1, j, rows, cols) + self.dfs_(grid, i, j-1, rows, cols) + self.dfs_(grid, i, j+1, rows, cols)

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

        def findCircleNum(self, M):
            n = len(M)
            result, visited = 0, [False] * n
            for i in range(n):
                if not visited[i]:
                    self._dfs(M, i, visited)
                    result += 1
            return result

        def _dfs(self, M, start, visited):
            visited[start] = True

            for i in range(len(M)):
                if M[start][i] and not visited[i]:
                    self.__dfs(M, i, visited)

        def trap(self, height):
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

        def partition(self, lists, low, high):
            if low == high:
                return lists[low]
            mid = low + ((high - low) >> 1)
            left = self.partition(lists, low, mid)
            right = self.partition(lists, mid+1, high)

        def merge(self, l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1 = self.merge(l1.next, l2)
                return l1
            else:
                l2 = self.merge(l1, l2.next)
                return l2

        def maxSubArray(self, nums):
            sub_sum = [0] * len(nums)
            sub_sum[0], max_sum = nums[0], nums[0]
            for i in range(1, len(nums)):
                if sub_sum[i-1] >= 0:
                    sub_sum[i] = sub_sum[i - 1] + nums[i]
                else:
                    sub_sum[i] = nums[i]
                max_sum = max(max_sum, sub_sum[i])
            return max_sum
