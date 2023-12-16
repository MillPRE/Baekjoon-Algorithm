from sys import stdin

N = int(stdin.readline())

dequeue = []

for _ in range(N):
    command = stdin.readline().split()
    if command[0] == "push_back":
        dequeue.append(command[1])
    if command[0] == "push_front":
        dequeue.insert(0, command[1])
    if command[0] == "pop_front":
        out = dequeue.pop(0) if len(dequeue) > 0 else -1
        print(out)
    if command[0] == "pop_back":
        out = dequeue.pop(len(dequeue) - 1) if len(dequeue) > 0 else -1
        print(out)
    if command[0] == "size":
        print(len(dequeue))
    if command[0] == "empty":
        print(1 if len(dequeue) == 0 else 0)
    if command[0] == "front":
        print(dequeue[0] if len(dequeue) > 0 else -1)
    if command[0] == "back":
        print(dequeue[-1] if len(dequeue) > 0 else -1)