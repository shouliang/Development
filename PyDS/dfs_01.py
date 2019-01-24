# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# https://www.programiz.com/dsa/graph-dfs
'''
The pseudocode for DFS is shown below.
In the init() function, notice that we run the DFS function on every node.
This is because the graph might have two different disconnected parts so to make sure that we cover every vertex,
we can also run the DFS algorithm on every node.

DFS(G, u)
    u.visited = true
    for each v ∈ G.Adj[u]         # 可能是非连通图，故要遍历对每个结点进行深度遍历
        if v.visited == false
            DFS(G,v)

init() {
    For each u ∈ G
        u.visited = false
    For each u ∈ G
        DFS(G, u)
}
'''


'''
极客时间-算法面试-DFS模板-递归版本 
visited = set()
def dfs(node,visited):
    visited.add(node)
    # process current node here

    if next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited) 
'''


# 深度遍历--递归版
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start]:         # 遍历当前元素所有相邻但未访问过的元素
        if next not in visited:
            dfs(graph, next, visited) # 将其中一个相邻但未访问过的元素，作为当前元素，继续递归遍历其相邻但未访问的元素
    return visited


# 深度遍历--非递归版，
# 与广度遍历的区别就是使用栈，从而利用栈的先进后出特点，也即后进先出
def _dfs(graph, start):
    visited, stack = set(), []
    visited.add(start)
    stack.append(start)

    while stack:
        vertex = stack.pop()        # 取栈顶元素，注意此处是pop()是后进先出，不同于bfs的pop(0)
        print(vertex)
        for next in graph[vertex]:  # 遍历相邻但未访问过的元素，并入栈
            if next not in visited:
                visited.add(next)
                stack.append(next)

    return visited


# 基于邻接表
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

visited = dfs(graph, 'A')
visited = _dfs(graph, 'A')
