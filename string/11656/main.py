data = input()
dic = []

for i in range(len(data)):
    dic.append(data[i:])

dic.sort()

for i in dic:
    print(i)