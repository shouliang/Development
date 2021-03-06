'''
朋友圈个数：
547. Friend Circles:https://leetcode.com/problems/friend-circles/
解释：
    班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
    如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
    给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
    如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

    示例 1:
    输入:
    [[1,1,0],
    [1,1,0],
    [0,0,1]]
    输出: 2
    说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
    第2个学生自己在一个朋友圈。所以返回2。

    示例 2:
    输入:
    [[1,1,0],
    [1,1,1],
    [0,1,1]]
    输出: 1
    说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。

注意：
    N 在[1,200]的范围内。
    对于所有学生，有M[i][i] = 1。
    如果有M[i][j] = 1，则有M[j][i] = 1。

思路：
    这道题让我们求朋友圈的个数，题目中对于朋友圈的定义是可以传递的，比如A和B是好友，B和C是好友，那么即使A和C不是好友，
    那么他们三人也属于一个朋友圈。那么比较直接的解法就是DFS搜索，对于某个人，遍历其好友，然后再遍历其好友的好友，
    那么我们就能把属于同一个朋友圈的人都遍历一遍，我们同时标记出已经遍历过的人，然后累积朋友圈的个数，
    再去对于没有遍历到的人在找其朋友圈的人，这样就能求出个数。
    其实这道题的本质是之前那道题Number of Connected Components in an Undirected Graph，
    其实许多题目的本质都是一样的，就是看我们有没有一双慧眼能把它们识别出来：
参考：https://www.cnblogs.com/grandyang/p/6686983.html    
'''


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)              # 邻接矩阵的len即为图中顶点的个数，此例中即为人员的个数
        res = 0
        visited = [False] * n   
        for i in range(n):       # 对每一个未访问过的顶点进行深度遍历
            if not visited[i]:
                self.dfs(M, i, visited)
                res += 1        # 某一个顶点深度遍历完毕后，朋友圈个数自增1
        return res

    def dfs(self, M, start, visited):
        visited[start] = True

        # 访问所有的邻居
        for i in range(len(M)):  # 遍历顶点与start相邻的顶点，且此顶点未被访问过
            if M[start][i] and visited[i] == False:
                self.dfs(M, i, visited)  # 递归调用


M1 = [[1, 1, 0],
      [1, 1, 0],
      [0, 0, 1]]

M2 = [[1, 1, 0],
      [1, 1, 1],
      [0, 1, 1]]

solution = Solution()
num1 = solution.findCircleNum(M1)
num2 = solution.findCircleNum(M2)
print(num1)
print(num2)
