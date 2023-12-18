import math

N = int(input())

for _ in range(N):
    case = list(map(int, input().split()))
    case = case[1:]
    result = 0
    for i in range(len(case)):
        for j in range(i+1, len(case)):
            result += math.gcd(case[i], case[j])
    print(result)
