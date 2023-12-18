N = int(input())
result = []

def sol(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i

while N > 1:
    r = sol(N)
    result.append(r)
    N = N // r

result.sort()

for n in result:
    print(n)