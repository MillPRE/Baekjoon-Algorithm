# A 진법 -> B 진법 변환
# 첫 줄 미래에서 사용하는 진법 A, 현재 사용 진법 B ( 2 ~ 30 )
# 두 째줄 -> A진법으로 나타낸 숫자의 자리수 m
# 세 째줄 -> A진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터 차례대로 주어진다.

# 17 8
# 2
# 2 16
a, b = map(int, input().split()) # A진법 ( 미래 ) B 진법 ( 현재 )
m = int(input()) # A진법 나타낸 자릿수
aList = list(map(int, input().split()))[::-1]

x = 0
# a진법 -> 10 진법
for i in range(len(aList)):
    x += aList[i] * (a ** i)

# 10진법 -> b 진법
result = []
while x != 0:
    result.append(x % b)
    x //= b
print(*result[::-1])