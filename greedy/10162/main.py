times = [300, 60, 10]
setting = [0, 0, 0]
T = int(input())

for i in range(len(times)):
    if T >= times[i]:
        n = int(T/times[i])
        T -= n * times[i]
        setting[i] = n

if T == 0:
    print(*setting, end=" ")
else:
    print(-1)