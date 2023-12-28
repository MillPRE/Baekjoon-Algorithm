n = int(input())
result = ""

if n == 0:
    print(0)
    exit()

while n != 0:
    print(n)
    if n % -2 == 0:
        result += "0"
        n = n // -2
    else:
        result += "1"
        n = n // -2 + 1

print(result[::-1])