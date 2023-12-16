from sys import stdin

stack_l = list(stdin.readline().strip())
stack_r = []

N = int(stdin.readline())

for _ in range(N):
    command = stdin.readline().split()
    if command[0] == "L":
        if len(stack_l) != 0:
            stack_r.append(stack_l.pop(-1))
    if command[0] == "D":
        if len(stack_r) != 0:
            stack_l.append(stack_r.pop(-1))
    if command[0] == "B":
        if len(stack_l) != 0:
            stack_l.pop(-1)
    if command[0] == "P":
        stack_l.append(command[1])
stack_r.reverse()
print("".join(stack_l) + "".join(stack_r))

