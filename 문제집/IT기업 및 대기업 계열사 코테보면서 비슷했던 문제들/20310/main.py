from sys import stdin

# 사전순 가장 빠른 것을 출력해야 하기 때문에
# 1은 왼쪽에서 부터 삭제, 0은 오른쪽에서부터 삭제
s = stdin.readline().strip()

count0 = s.count("0")//2
count1 = s.count("1")//2

while count0 > 0 or count1 > 0:
    if count1 > 0:
        idx1 = s.index("1")
        s = list(s)
        s[idx1] = ''
        s = "".join(s)
        count1 -= 1
    if count0 > 0:
        idx0 = s.rindex("0")
        s = list(s)
        s[idx0] = ''
        s = "".join(s)
        count0 -= 1

print("".join(s))



