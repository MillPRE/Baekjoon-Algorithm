from sys import stdin

string = stdin.readline().strip()
dic = [0 for i in range(26)]

# a 97 ~ z 122
for i in range(len(string)):
    dic[ord(string[i])-97] += 1

for i in range(len(dic)):
    print(dic[i], end=" ")