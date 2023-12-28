# Prefix Sum
from sys import stdin

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
prefix_sum = [0] + [0] * N # 0번 인덱스 사용 X

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    print(prefix_sum[b] - prefix_sum[a-1])