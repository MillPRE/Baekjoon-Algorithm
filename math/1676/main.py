N = int(input())

def fac(n):
    if n == 1 or n == 0:
        return 1
    return fac(n-1) * n

zero = 0
factorial = str(fac(N))[::-1]

for i in range(len(factorial)):
    if factorial[i] == '0':
        zero += 1
    else:
        break
print(zero)