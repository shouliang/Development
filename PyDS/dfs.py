# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# 深度搜索
def dfs(graph,start):
    visited, stack = set(),[start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# 深度搜索--递归版
def def_recursive(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

visited = dfs(graph,'A')


