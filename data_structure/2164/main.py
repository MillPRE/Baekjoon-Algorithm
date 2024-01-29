from sys import stdin
from collections import deque

N = int(stdin.readline())
if N == 1:
    print(1)
else:
    deq = deque([i for i in range(1, N+1)])
    while True:
        deq.popleft()
        if len(deq) == 1:
            break
        deq.append(deq.popleft())
    print(deq.pop())