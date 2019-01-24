# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# 广度优先搜索


def bfs(graph, start):
    visited, queue = set(), []
    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for i in graph[vertex]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    return visited


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

visited = bfs(graph, 'A')
