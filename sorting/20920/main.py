from sys import stdin

N, M = map(int, stdin.readline().split())
# print(N, M)
dicList = []
dic = {}


for _ in range(N):
    word = stdin.readline().strip()
    if len(word) >= M:
        dicList.append(word)
# print(dicList)

for word in dicList:
    if not word in dic:
        dic[word] = 1
    else:
        dic[word] += 1

keys = dic.keys()
# print(dic)
dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, count in dic:
    print(word)
