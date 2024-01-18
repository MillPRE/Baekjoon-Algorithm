from sys import stdin

# A 65
# Z 90
# 25

# a 97
# z 122

target = stdin.readline().strip()
dic = [0 for i in range(26)]

for t in target:
    if (ord(t) >= 97):
        dic[ord(t) - 65 - 32] += 1
    else:
        dic[ord(t) - 65] += 1

maxCnt = max(*dic)
if dic.count(maxCnt) > 1:
    print("?")
else:
    print(chr(dic.index(maxCnt) + 65))