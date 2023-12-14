# 메모리 제한으로 sort 사용 못함.

from sys import stdin
MAX = 10001
N = int(stdin.readline())
data = [0] * MAX

for _ in range(N):
    data[int(stdin.readline())] += 1

for i in range(MAX):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)