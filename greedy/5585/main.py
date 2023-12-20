pay = int(input())
count = 0

change = 1000 - pay

ens = [500, 100, 50, 10, 5, 1]

for en in ens:
    if change >= en:
        count += change // en
        change -= en * (change // en)

print(count)