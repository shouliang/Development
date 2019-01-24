# https://www.programiz.com/dsa/graph-bfs

''' BFS伪代码
BFS pseudocode
create a queue Q
mark v as visited and put v into Q
while Q is non-empty
    remove the head u of Q
    mark and enqueue all (unvisited) neighbours of u
'''

'''
极客时间-算法面试-bfs模板，bfs只有使用队列这种数据结构的非递归版本一种，无递归版本，而dfs有递归和非递归两种版本
bfs利用队列先进先出的特点，在弹出节点以后，将该节点的相邻结点再加入队列，在二叉树中其实就是左右孩子
def bfs(graph, start):
    visited,queue = set(),[]
    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        visited.add(node)

        process(node)                         # 处理结点：譬如打印结点或者将结点添加到一个数组里面存储起来
        nodes = generate_related_nodes(node)  # 遍历结点的所有未访问的相邻结点，并相继入队列
        queue.append(nodes)
'''


'''
邻接表： bfs_01和bfs_02访问标记分别使用数组和set()
图的存储结构是邻接表的形式，在python里面是通过字典来实现，如：graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
标记顶点已经被访问的集合：通过数组这种数据结构，顶点类型只能是数字，否则visited[start]会报错
                      通过set这种数据结构,顶点的类型为数字和字符均可
'''


def bfs_01(graph, start):
    visited, queue = [False] * len(graph), []
    visited[start] = True
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)                  # 处理结点：譬如打印结点或者将结点添加到一个数组里面存储起来
        for neighbour in graph[vertex]:
            if visited[neighbour] is False:
                visited[neighbour] = True
                queue.append(neighbour)


def bfs_02(graph, start):
    visited,  queue = set(), []
    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# ------------------------------------------------------------------------------------------


'''
邻接矩阵： bfs_03和bfs_04访问标记分别使用数组和set()
针对图的存储结构是邻接矩阵的形式，通过二维数组的形式来实现，graph[i][j] == 1表示顶点i和顶点j相连接，所以肯定是数字类型，不存在字符类型
标记顶点已经被访问的集合：通过数组这种数据结构
                      通过set这种数据结构
'''


def bfs_03(graph, start):
    visited, queue = [False] * len(graph), []
    visited[start] = True
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)

        # 关键点是找出vertex的邻接点，在邻接矩阵中需要遍历所有的顶点
        for i in range(len(graph)):
            if graph[vertex][i] == 1 and not visited[i]:  # graph[vertex][i] == 1：表示顶点vertex和i连接
                visited[i] = True
                queue.append(i)


# 针对图的存储结构是邻接矩阵的形式，通过二维数组的形式来实现,graph[i][j] == 1表示顶点i和顶点j相连接，所以肯定是数字类型，不存在字符类型
# 标记顶点已经被方法的集合：通过set这种数据结构
def bfs_04(graph, start):
    visited, queue = set(), []
    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for i in range(len(graph)):
            # graph[vertex][i] == 1：表示顶点vertex和i连接
            if graph[vertex][i] == 1 and i not in visited:
                visited.add(i)
                queue.append(i)


# test
graph1 = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}  # 图：邻接表的存储方式，图中顶点类型为数字
graph2 = {'a': ['b', 'c'], 'b': ['c'], 'c': [
    'd'], 'd': ['b', 'c']}                       # 图：邻接表的存储方式，图中顶点类型为字符

# bfs_01只能变量顶点是数字类型的图
bfs_01(graph1, 0)

# bfs_02可以遍历顶点是数字或者字符类型的图
bfs_02(graph1, 0)
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
