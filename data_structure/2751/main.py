from sys import stdin

N = int(stdin.readline())

data = []
for _ in range(N):
    data.append(int(stdin.readline()))

data.sort()

for i in range(N):
    print(data[i])