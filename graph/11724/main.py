from sys import stdin

N, M = map(int, stdin.readline().split())
E = {}

for i in range(1, N+1):
    E[i] = []


for i in range(M):
    a, b = map(int, stdin.readline().split())
    E[a].append(b)
    E[b].append(a)

visited = [-1] + [0] * (N)
team = 0

while True:
    if visited.count(1) == N:
        break
    start = visited.index(0)

    stack = [start]

    while len(stack) > 0:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            for i in range(len(E[v])):
                if visited[E[v][i]] == 0:
                    stack.append(E[v][i])
    team += 1

print(team)
