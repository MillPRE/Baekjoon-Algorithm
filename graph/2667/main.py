h = int(input())
matrix = []
for _ in range(h):
    matrix.append(list(map(int, input())))
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 단지 수
danzi = 0
def bfs(coordinate):
    # coordinate = (y, x)
    queue = [coordinate]
    mCount = 0 # 하나의 단지의 수

    while len(queue) > 0:
        v = queue.pop(0)
        if matrix[v[0]][v[1]] == 1:
            mCount += 1
            matrix[v[0]][v[1]] = 0

            for i in range(len(dx)):
                if v[0]+dy[i] >= 0 and v[0]+dy[i] < len(matrix) and v[1] + dx[i] >= 0 and v[1] + dx[i] < len(matrix[0]):
                    queue.append((v[0]+dy[i], v[1]+dx[i]))
    return mCount

result = []
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == 1:
            result.append(bfs((y, x)))
            danzi += 1
result.sort()
print(danzi)
for n in result:
    print(n)