H, W = map(int, input().split())
stand = 4

# 1. 세로 1 -> 1
if H == 1:
    print(1)
elif H == 2 and W <= 7:
    # 2. 세로 2 and 가로 M
    print(min(stand, (W+1)//2))
elif H == 3 and W < 7:
    # 3. H == 3 and W < 7:
    print(min(stand, W))
elif H > 3 and W < 7:
    print(min(stand, W))
elif H == 2:
    print(min(stand, W))
else:
    print(W-2)