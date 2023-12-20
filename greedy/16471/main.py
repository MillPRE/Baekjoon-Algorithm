from sys import stdin

N = int(stdin.readline())
A = sorted(list(map(int, stdin.readline().split())), reverse=True)
B = sorted(list(map(int, stdin.readline().split())))

win = 0

for a in A:
    if a >= B[-1]:
        pass
    else:
        win += 1
        B.pop()

print("YES" if int((N+1)//2) <= win else "NO")

