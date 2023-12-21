while True:
    try:
        n = int(input())
        i = 0
        while True:
            i += 1
            m = "1" * i
            if int(m) % n == 0:
                print(len(m))
                break
    except EOFError:
        break

# 1, 11, 111, 1111 ... 의 갯수가 n * i 들의 수보다 적다.
# 시간 초과
# while True:
#     try:
#         n = int(input())
#         i = 1
#         while True:
#             i += 1
#             m = n * i
#             _set = set(str(m))
#             if len(_set) == 1 and _set.pop() == "1":
#                 print(len(str(m)))
#                 break
#     except EOFError:
#         break