from sys import stdin

MOD = 10007

def dp_function(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if dp[x] != 0:
        return dp[x]
    dp[x] = dp_function(x - 1) + dp_function(x - 2)
    return dp_function(x - 1) + dp_function(x - 2)

x = int(stdin.readline())
dp = [0 for _ in range(x+1)]

print(dp_function(x) % MOD)
