from sys import stdin

N = int(stdin.readline().strip())
head = [-1,-1]
heart = [-1, -1]
result = []
cookies = []

for row in range(N):
    newLine = list(stdin.readline().strip())
    cookies.append(newLine)
    for col in range(len(newLine)):
        # 쿠키 머리 index 저장
        if head[0] == -1 and head[1] == -1 and newLine[col] == '*':
            head[0] = row+1
            head[1] = col+1
            # 머리 기준 바로 아래 심장
            heart[0] = head[0] + 1
            heart[1] = head[1]
            break

# 왼팔 심장 기준 왼쪽
cookie_length = 0
for col in range(0, heart[1]-1):
    if cookies[heart[0]-1][col] == "*":
        cookie_length += 1
result.append(cookie_length)

# 오른팔 심장 기준 오른쪽
cookie_length = 0
for col in range(heart[1], N):
    if cookies[heart[0]-1][col] == "*":
        cookie_length += 1
    else:
        break
result.append(cookie_length)

# 허리 심장 기준 아래
waist_last = [-1, -1]
cookie_length = 0
for row in range(heart[0], N):
    if cookies[row][heart[1]-1] == "*":
        cookie_length += 1
    else:
        waist_last[0] = row-1
        waist_last[1] = heart[1]-1
        break
result.append(cookie_length)


left = 0
right = 0
for row in range(waist_last[0]+1, N):
    # 왼다리 허리 마지막 인덱스 기준 대각선 왼쪽 아래
    # waist_last[0]+1 waist_last[1]-1
    if cookies[row][waist_last[1]-1] == "*":
        left += 1
    # 오른다리 허리 마지막 인덱스 기준 대각선 오른쪽 아래
    # waist_last[0]+1 waist_last[1]+1
    if cookies[row][waist_last[1] + 1] == "*":
        right += 1
result.append(left)
result.append(right)

print(*heart)
print(*result)