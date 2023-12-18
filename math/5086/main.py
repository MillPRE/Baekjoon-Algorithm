from sys import stdin

n1, n2 = -1, -1
while n1 != 0 and n2 != 0:
    n1, n2 = map(int, stdin.readline().split())
    if n1 == 0 and n2 == 0 :
        break
    if n2 % n1 == 0:
        print("factor")
    elif n1 % n2 == 0:
        print("multiple")
    else:
        print("neither")