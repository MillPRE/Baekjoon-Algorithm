N = int(input())
rope = []

for _ in range(N):
    rope.append(int(input()))

rope.sort()

result = []
cnt = N

for r in rope:
    result.append(r*cnt)
    cnt -= 1
print(max(result))