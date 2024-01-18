from sys import stdin

# 상근 SK 선
# 창영 CY

# N % 3 ==0
# 몫 짝수 상근
# 몫 홀수 창영

# N % 3 !=0
# 몫 짝수 나머지 1 상근
# 몫 짝수 나머지 2 창영
# 몫 홀수 나머지 1 창영
# 몫 홀수 나머지 2 상근

N = int(stdin.readline())

if N % 3 == 0 and (N // 3) % 2 == 0:
    print("CY")
elif N % 3 == 0:
    print("SK")
elif N % 3 != 0 and (N//3) % 2 == 0 and (N%3) == 1:
    print("SK")
elif N % 3 != 0 and (N//3) % 2 == 0 and (N%3) == 2:
    print("CY")
elif N % 3 != 0 and (N//3) % 2 == 1 and (N%3) == 1:
    print("CY")
elif N % 3 != 0 and (N//3) % 2 == 1 and (N%3) == 2:
    print("SK")