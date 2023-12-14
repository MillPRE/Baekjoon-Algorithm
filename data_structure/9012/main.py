from sys import stdin

def solution(pararm):
    data = map(str, pararm.strip())

    stack = []
    for d in data:
        if d == "(":
            stack.append(d)
        elif len(stack) == 0:
            return False
        elif stack[-1] == "(":
            stack.pop()
        else:
            stack.append(d)

    return True if len(stack) == 0 else False

N = int(stdin.readline())

for _ in range(N):
    print("YES" if solution(stdin.readline()) else "NO")
