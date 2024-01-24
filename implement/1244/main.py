import math
from sys import stdin

# N개의 스위치 상태가 주어짐
# 남자 - 스위치 번호가 자기가 받은 수의 배수면 그 스위치의 상태 바꿈
# ex 남학생 3 -> 3번 6번 스위치의 상태를 바꿈
# 여자 - 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아
# 구간에 속하는 스위치의 상태를 모두 바꾼다. (구간에 속한 스위치 개수는 항상 홀수)

N = int(stdin.readline())
switch = list(map(int, stdin.readline().split()))

T = int(stdin.readline())

for _ in range(T):
    sex, number = map(int, stdin.readline().split())
    if sex == 1:
        # 본인이 받은 스위치의 번호의 배수 상태 변경
        # print("남자")
        multi = 1
        while True:
            index = multi * number
            if index-1 < len(switch):
                switch[index-1] = 1 if switch[index-1] == 0 else 0
                multi += 1
            else:
                break
        # print(switch)
    else:
        # print("여자")
        # 본인이 받은 수 기준 대칭 가장 많은 스위치 포함 구간 상태 변셩
        middle = number - 1
        left = middle - 1
        right = middle + 1

        while True:
            # out of range check
            if left < 0 or right >= len(switch):
                left += 1
                right -= 1
                break
            # 대칭 체크
            if switch[left] == switch[right]:
                left -= 1
                right += 1
            else:
                left += 1
                right -= 1
                break
        if left != middle and right != middle:
            for i in range(left, right+1):
                switch[i] = 1 if switch[i] == 0 else 0
        else:
            switch[middle] = 1 if switch[middle] == 0 else 0
        # print(switch)

for i in range(math.ceil(len(switch)/20)):
    print(*switch[i*20: (i+1)*20])
