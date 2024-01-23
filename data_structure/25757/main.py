from sys import stdin

N, G = map(str, stdin.readline().split())
user = []

for _ in range(int(N)):
    user.append(stdin.readline().strip())

user = set(user)
if G == "F":
    print(len(user)//2)
elif G == "O":
    print(len(user)//3)
else:
    print(len(user))