from sys import stdin

dic = {}

N = int(stdin.readline())

for _ in range(N):
    n = int(stdin.readline())
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1

data = [v for v in dic.values()]
n = max(data)

data.clear()

for key in dic.keys():
    if dic[key] == n:
        data.append(key)
print(min(data))