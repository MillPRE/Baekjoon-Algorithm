from collections import deque

N, K = map(int, input().split())
dequeN = deque([i for i in range(1, N+1)])
cur = -1
result = []

while len(result) < N:
#    print(dequeN) -> 출력해서 확인하면 로직 확인 쉬움
    right = []
    if len(dequeN) >= K:
        for i in range(K-1):
            right.append(dequeN.popleft())
        dequeN.extend(right)
        result.append(dequeN.popleft())
    elif len(dequeN) > 1:
        idx = 0
        cnt = 1
        while cnt < K:
            idx += 1
            if idx >= len(dequeN):
                idx = 0
            cnt += 1
        for i in range(idx):
            right.append(dequeN.popleft())
        dequeN.extend(right)
        result.append(dequeN.popleft())
    else:
        result.append(dequeN.popleft())

# 출력 구간
print("<", end="")
for i in range(0, N-1):
    print(result[i], end=", ")
print(f"{result[-1]}>")