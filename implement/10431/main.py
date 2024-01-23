from sys import stdin

T = int(stdin.readline().strip())

for _ in range(T):
    arr = list(map(int, stdin.readline().strip().split()))
    num = arr[0]
    arr = arr[1:]

    newArr = []
    count = 0

    for a in arr:
        if len(newArr) == 0:
            newArr.append(a)
        else:
            for idx in range(1, len(newArr)+1):
                if newArr[-idx] > a:
                    count += 1

                    if idx == len(newArr):
                        newArr.insert(0, a)
                else:
                    if idx == 1:
                        newArr.append(a)
                        break
                    else:
                        # print(a, idx)
                        newArr = newArr[:-(idx -1)] + [a] + newArr[-(idx - 1):]
                        break
        # print(a, newArr, count)
    print(num, count)
