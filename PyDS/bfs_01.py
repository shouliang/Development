# https://www.programiz.com/dsa/graph-bfs

''' BFS伪代码
BFS pseudocode
create a queue Q
mark v as visited and put v into Q
while Q is non-empty
    remove the head u of Q
    mark and enqueue all (unvisited) neighbours of u
'''


# 针对图的存储结构是邻接表的形式，在python里面是通过字典来实现，如：graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
# 标记顶点已经被访问的集合：通过数组这种数据结构，顶点类型只能是数字，否则visited[start]会报错
def bfs_01(graph, start):
    visited = [False] * len(graph)
    queue = []
    visited[start] = True
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for neighbour in graph[vertex]:     # 关键点是找出顶点vertex的邻接顶点，通过遍历，命名为邻居节点，似乎好理解一点
            if visited[neighbour] is False:
                visited[neighbour] = True
                queue.append(neighbour)

# 针对图的存储结构是邻接表的形式，在python里面是通过字典来实现，如：graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
# 标记顶点已经被方法的集合：通过set这种数据结构,顶点的类型为数字和字符均可
def bfs_02(graph, start):
    visited = set()
    queue = []
    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# 针对图的存储结构是邻接矩阵的形式，通过二维数组的形式来实现，graph[i][j] == 1表示顶点i和顶点j相连接，所以肯定是数字类型，不存在字符类型
# 标记顶点已经被访问的集合：通过数组这种数据结构
def bfs_03(graph, start):
    visited = [False] * len(graph)
    queue = []
    visited[start] = True
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for i in range(len(graph)):                       # 关键点是找出vertex的邻接点，在邻接矩阵中需要遍历所以的顶点
            if graph[vertex][i] == 1 and not visited[i]:  # graph[vertex][i] == 1：表示顶点vertex和i连接
                visited[i] = True
                queue.append(i)


# 针对图的存储结构是邻接矩阵的形式，通过二维数组的形式来实现,graph[i][j] == 1表示顶点i和顶点j相连接，所以肯定是数字类型，不存在字符类型
# 标记顶点已经被方法的集合：通过set这种数据结构
def bfs_04(graph, start):
    visited = set()
    queue = []
    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for i in range(len(graph)):
            if graph[vertex][i] == 1 and i not in visited:  # graph[vertex][i] == 1：表示顶点vertex和i连接
                visited.add(i)
                queue.append(i)


graph1 = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}  # 图：邻接表的存储方式，图中顶点类型为数字
graph2 = {'a': ['b', 'c'], 'b': ['c'], 'c': ['d'], 'd': ['b', 'c']}  # 图：邻接表的存储方式，图中顶点类型为字符

bfs_01(graph1, 0)  # bfs_01只能变量顶点是数字类型的图
bfs_02(graph1, 0)  # bfs_02，可以遍历顶点是数字或者字符类型的图
bfs_02(graph2, 'a')

# 图：邻接矩阵形式
graph3 = [
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]
bfs_03(graph3, 0)
bfs_04(graph3, 0)
