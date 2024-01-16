N = int(input())
arr = list(map(int, input().split()))

arrToSet = set(arr)
arr = list(arrToSet)
arr.sort()
print(*arr)