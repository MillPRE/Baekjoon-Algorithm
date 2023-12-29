from sys import stdin
# 섬은 가로, 세로, 대각선 연결
# 좌 대각선, 상, 우 대각선
# 좌,          우
# 좌 대각선, 하, 우 대각선
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(island, x, y):
    queue = [(y, x)]

    while len(queue) > 0:
        y, x = queue.pop(0)
        if island[y][x] == 1:
            island[y][x] = 0
            for i in range(len(dx)):
                newY = y + dy[i]
                newX = x + dx[i]
                if newY >= 0 and newY < len(island) and newX >= 0 and newX < len(island[0]) and island[newY][newX] == 1:
                    queue.append((newY, newX))
    return island

while True:
    island = []
    w, h = map(int, stdin.readline().split()) # 섬 크기 입력
    if w == 0 or h == 0:
        break

    # 섬 세팅
    for i in range(h):
        island.append(list(map(int, stdin.readline().split())))
    # 섬 개수
    count = 0
    # 탐색
    # bfs
    for y in range(len(island)):
        for x in range(len(island[0])):
            if island[y][x] == 1:
                island = bfs(island, x, y)
                count += 1

    print(count)
