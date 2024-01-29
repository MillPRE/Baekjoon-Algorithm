# N 굴다리의 길이
# M 가로등의 수
# x 가로등 설치 위치
import math
from sys import stdin
N = int(stdin.readline())
lamp = [0 for i in range(N+1)]

M = int(stdin.readline())
xList = list(map(int, stdin.readline().split()))

for x in xList:
    lamp[x] = 1
# print(lamp)

maxLen = 0
if M == 1:
    maxLen = max(xList[0], N-xList[0])
else:
    for idx in range(len(xList)):
        leftIdx = -1
        # 왼쪽 가로등 길이 계산
        if idx == 0:
            # idx == 0 이면 xList[idx] 위치 전에는 가로등이 없음
            # 오른쪽 위치 - 왼쪽 위치
            leftIdx = 0
            maxLen = max(maxLen, xList[idx] - leftIdx)
        else:
            # idx != 0 이면 xList[idx-1] 존재
            leftIdx = xList[idx-1]
            # (오른쪽 - 왼쪽) / 2
            maxLen = max(maxLen, math.ceil((xList[idx] - leftIdx)/2))

        # 오른쪽 가로등 길이 계산
        if idx + 1 < len(xList):
            # 뒤로 가로등 있는 경우
            rightIdx = xList[idx+1]
            maxLen = max(maxLen, math.ceil((rightIdx - xList[idx])/2))
        else:
            # 뒤로 가로등 없는 경우
            rightIdx = len(lamp) -1
            maxLen = max(maxLen, rightIdx - xList[idx])

print(maxLen)
