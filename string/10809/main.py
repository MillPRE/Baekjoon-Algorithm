from sys import stdin

string = stdin.readline().strip()
dic = [-1 for i in range(26)]

for idx in range(len(string)):
    if dic[ord(string[idx]) - 97] == -1:
        dic[ord(string[idx]) - 97] = idx

for i in range(len(dic)):
    print(dic[i], end=" ")