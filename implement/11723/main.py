from sys import stdin

T = int(stdin.readline())
S = []

for _ in range(T):
    commands = list(map(str, stdin.readline().split()))
    if commands[0] == "add" and S.count(int(commands[1])) < 1:
        S.append(int(commands[1]))
    elif commands[0] == "remove" and S.count(int(commands[1])) >= 1:
        S.remove(int(commands[1]))
    elif commands[0] == "check":
        print( 1 if S.count(int(commands[1])) >= 1 else 0)
    elif commands[0] == "toggle" and S.count(int(commands[1])) < 1:
        S.append(int(commands[1]))
    elif commands[0] == "toggle" and S.count(int(commands[1])) >= 1:
        S.remove(int(commands[1]))
    elif commands[0] == "all":
        S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif commands[0] == "empty":
        S = []