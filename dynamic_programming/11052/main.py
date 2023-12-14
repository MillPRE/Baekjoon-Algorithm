# Input
# 4 -> N
# 1 5 6 7 -> Pi List
# 첫째 줄에 민규가 구매하려고 하는 카드의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)
# 둘째 줄에는 Pi가 P1부터 PN까지 순서대로 주어진다. (1 ≤ Pi ≤ 10,000)

# Output: 카드 N개 구매하는 최대값

N = int(input())
Pi = list(map(int, input().split()))
Pi.insert(0,0)
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], Pi[j] + dp[i-j])
print(dp[N])


