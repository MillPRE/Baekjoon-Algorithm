N = int(input())

data = []
for _ in range(N):
    age, name = map(str, input().split())
    data.append((int(age), name))

data.sort(key = lambda x: x[0])

for age, name in data:
    print(age, name)
