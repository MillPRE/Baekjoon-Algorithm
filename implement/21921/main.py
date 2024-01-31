from sys import stdin

N, X = map(int, stdin.readline().split())
visited = list(map(int, stdin.readline().split()))


intervalSum = sum(visited[0: X])
maxVisit = intervalSum
maxVisitCount = 1

for i in range(1, N - X + 1):
    intervalSum = intervalSum - visited[i-1] + visited[i+X-1]
    if intervalSum > maxVisit:
        maxVisit = intervalSum
        maxVisitCount = 1
    elif intervalSum == maxVisit:
        maxVisitCount += 1

if maxVisit == 0:
    print("SAD")
else:
    print(maxVisit)
    print(maxVisitCount)