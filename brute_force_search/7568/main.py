from sys import stdin

N = int(stdin.readline())
p = []
rank = [0 for i in range(N)]

for _ in range(N):
    p.append(list(map(int, stdin.readline().split())))

idx = 0
while True:
    if idx == N:
        break
    r = 1
    for i in range(N):
        if i == idx:
            pass
        if p[idx][0] < p[i][0] and p[idx][1] < p[i][1]:
            r += 1
    rank[idx] = r
    idx += 1

print(*rank)

