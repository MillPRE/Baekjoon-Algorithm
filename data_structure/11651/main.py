from sys import stdin

N = int(stdin.readline())

data = []

for _ in range(N):
    x, y = map(int, stdin.readline().split())
    data.append((x,y))

data.sort(key=lambda x: (x[1], x[0]))

for x, y in data:
    print(x, y)