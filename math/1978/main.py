N = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(len(arr)):
    cnt = 0
    for n in range(2, arr[i]+1):
        if arr[i] % n == 0:
            cnt += 1
    if cnt == 1:
        result += 1
print(result)