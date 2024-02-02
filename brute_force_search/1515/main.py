
from sys import stdin

N = stdin.readline().strip()
cur = 1
index = 0
while True:
    num = str(cur)
    for n in num:
        if index < len(str(N)) and n == str(N[index]):
            index += 1
    if index >= len(str(N)):
        break
    cur += 1

print(cur)