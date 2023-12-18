import math
a, b = map(int, input().split())

print("".join(["1" for i in range(math.gcd(a, b))]))