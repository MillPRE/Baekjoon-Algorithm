import sys
input = sys.stdin.readline
N = int(input())

last = 0
stack = []
result = ""

for _ in range(N):
    n = int(input())
    if len(stack) == 0 or (len(stack) > 0 and stack[-1] != n):
        for i in range(last+1, n+1):
            stack.append(i)
            result += "+\n"
        stack.pop()
        result += "-\n"
        last = n
    else:
        stack.pop()
        result += "-\n"
if len(stack) > 0:
    print("NO")
else:
    print(result)