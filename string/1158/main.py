from sys import stdin

N, K = map(int, stdin.readline().split())

queue = [i for i in range(1, N+1)]
cur = K-2

stack = []
while len(queue) != 0:
    stack.append(queue.pop(cur))
