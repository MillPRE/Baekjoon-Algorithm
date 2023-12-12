# N은 1보다 크고, 10^6 보다 작거나 같음.
N = int(input())
dp = [0] * 1000001

for n in range(2, N+1):
    if n % 6 == 0:
        dp[n] = min(dp[n//2], dp[n//3], dp[n-1]) + 1
    elif n % 2 == 0:
        dp[n] = min(dp[n // 2], dp[n - 1]) + 1
    elif n % 3 == 0:
        dp[n] = min(dp[n // 3], dp[n - 1]) + 1
    else:
        dp[n] = dp[n-1] + 1

print(dp[N])