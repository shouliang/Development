# https://www.programiz.com/dsa/graph-dfs
'''
The pseudocode for DFS is shown below.
In the init() function, notice that we run the DFS function on every node.
This is because the graph might have two different disconnected parts so to make sure that we cover every vertex,
we can also run the DFS algorithm on every node.

DFS(G, u)
    u.visited = true
    for each v ∈ G.Adj[u]
        if v.visited == false
            DFS(G,v)

init() {
    For each u ∈ G
        u.visited = false
    For each u ∈ G
        DFS(G, u)
}
'''

def dfs(graph, start,visited =None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)    # 递归访问下一个顶点
    return visited

graph = {
    '0':set(['1','2']),
    '1':set(['0','3','4']),
    '2':set(['0']),
    '3':set(['1']),
    '4':set(['2','3'])
}

dfs(graph,'0')