N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
total = 0

while len(A) > 0:
    aMax = max(A)
    bMin = min(B)
    A.remove(aMax)
    B.remove(bMin)
    total += aMax * bMin
print(total)
