# A -> 10, B -> 11, C -> 12, ... F -> 15,  ... Y -> 34, Z -> 35
# A -> 65, Z ->90
# ord - 55
# B ( 2 <= B <= 36 )

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
answer = ""

while N != 0:
    answer += str(tmp[N % B])
    N = N // B
print(answer[::-1])
