def BFS(graph, node):
    visited = [False] * len(graph)
    queue = [node]
    visited[node] = True
    while queue:
        vertex = queue.pop(0)
        print(vertex, end = ' ')
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))
graph = [[] for _ in range(n)]
for i in range(e):
    u = int(input("Enter u: "))
    v = int(input("Enter v: "))
    graph[u].append(v)

BFS(graph, 0)
