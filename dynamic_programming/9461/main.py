# keyword: memozation
# memozation 사용하지 않으면 시간초과
# DP 할때 메모제이션 사용하기**

memo = {}
def function(n):
    if n in memo:
        return memo[n]

    if n < 4:
        memo[n] = 1
        return 1
    if n < 6:
        memo[n] = 2
        return 2
    else:
        memo[n] = function(n-1) + function(n-5)
    return memo[n]

T = int(input())

for i in range(T):
    N = int(input())
    if N < 4:
        print(1)
    elif N < 6:
        print(2)
    else:
        print(function(N))



