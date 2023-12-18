# A -> 10, B -> 11, C -> 12, ... F -> 15,  ... Y -> 34, Z -> 35
# A -> 65, Z ->90
# ord - 55
# B ( 2 <= B <= 36 )

target, B = map(str, input().split())
result = 0

for i in range(len(target)):
    if target[i].isnumeric():
        result += int(B) ** (len(target) - i-1) * int(target[i])
    else:
        result += int(B) ** (len(target) - i-1) * (ord(target[i]) - 55)
print(result)