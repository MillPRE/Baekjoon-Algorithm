from sys import stdin
M, N = map(int, stdin.readline().split())

def is_prime(n):
    end = int(n ** 0.5)
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

for i in range(M, N+1):
    if is_prime(i) and i != 1:
        print(i)