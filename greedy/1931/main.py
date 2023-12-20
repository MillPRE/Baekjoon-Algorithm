N = int(input())
times = []
dic = {}

for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: (x[0], x[1]), reverse=True)
result = [times[0]]

for i in range(1, len(times)):
    if result[-1][0] >= times[i][1]:
        result.append(times[i])


print(len(result))