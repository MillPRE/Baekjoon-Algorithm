p = []
for _ in range(9):
    p.append(int(input()))

for i in range(9):
    for j in range(i+1, 9):
        temp = [*p]
        temp.remove(p[i])
        temp.remove(p[j])
        if sum(temp) == 100:
            p = [*temp]
            break
    if len(p) == 7:
        break
p.sort()
print(*p, end="\n")