# DFS 수행결과 출력
# BFS 수행결과 출력

N, M, V = map(int, input().split())
graph = {}

for _ in range(M):
    a, b = map(int, input().split())
    if graph.get(a):
        graph[a].append(b)
    else:
        graph[a] = [b]

    if graph.get(b):
        graph[b].append(a)
    else:
        graph[b] = [a]

def dfs(g, s):
    visited = [s]
    if not g.get(s):
        return visited
    g[s].sort(reverse=True)
    stack = [*g[s]]

    while len(stack) > 0:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            g[v].sort(reverse=True)
            for i in range(len(g[v])):
                stack.append(g[v][i])
    return visited


def bfs(g, s):
    visited = [s]
    if not g.get(s):
        return visited
    g[s].sort()
    queue = [*g[s]]

    while len(queue) > 0:
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            g[v].sort()
            for i in range(len(graph[v])):
                queue.append(graph[v][i])
    return visited

print(*dfs(graph, V), end=" ")
print("")
print(*bfs(graph, V), end=" ")
