from sys import stdin

n = int(stdin.readline())
dp = [0 for _ in range(n+1)]

def _dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if dp[n] != 0:
        return dp[n]
    dp[n] = _dp(n-1) + _dp(n-2) * 2
    return dp[n]

print(_dp(n) % 10007)