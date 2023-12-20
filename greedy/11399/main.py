N = int(input())
times = list(map(int, input().split()))

times.sort()
totalTime = 0
curTime = 0

for time in times:
    curTime += time
    totalTime += curTime
print(totalTime)