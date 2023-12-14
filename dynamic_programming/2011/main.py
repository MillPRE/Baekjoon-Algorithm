# Input
# 첫째 줄에 5000자리 이하의 암호가 주어진다. 암호는 숫자로 이루어져 있다.

# Output
# 나올 수 있는 해석의 가짓수를 구하시오. 정답이 매우 클 수 있으므로, 1000000으로 나눈 나머지를 출력한다.
# 암호가 잘못되어 암호를 해석할 수 없는 경우에는 0을 출력한다.

N = list(map(int,input()))
LENGTH = len(N)
dp = [0 for _ in range(LENGTH+1)]

if (N[0] == 0) :
    print("0")
else :
    n = [0] + N
    dp[0]=dp[1]=1
    for i in range(2, LENGTH+1):
        if n[i] > 0:
            dp[i] += dp[i-1]
        temp = n[i-1] * 10 + n[i]
        if temp >= 10 and temp <= 26 :
            dp[i] += dp[i-2]
    print(dp[LENGTH] % 1000000)

