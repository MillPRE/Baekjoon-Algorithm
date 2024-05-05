from sys import stdin

N, M = map(int, stdin.readline().strip().split())

powers = []

for _ in range(N):
    title, power = map(str, stdin.readline().strip().split())
    powers.append([title, int(power)])


powers.sort(key=lambda x: x[1]) # 오름차순 정렬

for _ in range(M):
    power = int(stdin.readline().strip())
    start = 0
    end = len(powers)-1

    while start <= end:
        mid = (start+end) // 2
        if power > powers[mid][1]:
            start = mid + 1
        else:
            end = mid - 1

    print(powers[start][0])

