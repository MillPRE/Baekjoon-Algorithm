from sys import stdin

# 소수
MAX = 1000001
prime = [True] * MAX
end = int(MAX ** 0.5)

for i in range(2,end+1):
    if prime[i]:
        for k in range(i+i, MAX, i):
            prime[k] = False

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    for i in range(3, len(prime), 2):
        if prime[i] and prime[n-i]:
            print("%d = %d + %d" % (n, i, n - i))
            break