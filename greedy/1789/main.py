S = int(input())
# 1 <= S <= 4,294,967,295
i = 1
count = 1
while True :
    S-= i
    if S < 0:
        break
    i += 1
    count += 1
print(count-1)