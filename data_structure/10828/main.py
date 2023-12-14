from sys import stdin

N = int(stdin.readline())
stack = []

for _ in range(N):
    command = list(map(str, stdin.readline().split()))
    if command[0] == 'top':
        print( -1 if len(stack) == 0 else stack[len(stack)-1])
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'pop':
        print(-1 if len(stack) == 0 else stack.pop())
    elif command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    else:
        stack.append(int(command[1]))