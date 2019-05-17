import heapq


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left and right:
                return root
            return left if left else right

    def lowestCommonAncestor_01(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor_01(root.left, p, q)
        right = self.lowestCommonAncestor_01(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def lowestCommonAncestor_02(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor_02(root.left, p, q)
        right = self.lowestCommonAncestor_02(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def findKthLargest(self, nums, k):
        top_nums = []
        for i in range(len(nums)):
            if len(top_nums) < k:
                heapq.heappush(top_nums, nums[i])
            elif top_nums[0] < nums[i]:
                heapq.heappushpop(top_nums, nums[i])
        return top_nums[0]

    def findKthLargest_01(self, nums, k):
        top_nums = []
        for i in range(len(nums)):
            if len(top_nums) < k:
                heapq.heappush(top_nums, nums[i])
            elif top_nums[0] < nums[i]:
                heapq.heappushpop(top_nums, nums[i])
        return top_nums[0]

    def findKthLargest_02(self, nums, k):
        top_nums = []
        for i in range(len(nums)):
            if len(top_nums) < k:
                heapq.heappush(top_nums, nums[i])
            elif top_nums[0] < nums[i]:
                heapq.heappushpop(top_nums, nums[i])

