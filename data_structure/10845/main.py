# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# Input
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# Output
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# 시간초과 개선을 위해서 stdin

from sys import stdin
N = int(stdin.readline())

QUEUE = []

for i in range(N):
    command = list(map(str, stdin.readline().split()))

    if command[0] == 'front':
        print(-1 if len(QUEUE) == 0 else QUEUE[0])
    elif command[0] == 'back':
        print( -1 if len(QUEUE) == 0 else QUEUE[-1])
    elif command[0] == 'size':
        print(len(QUEUE))
    elif command[0] == 'pop':
        print( -1 if len(QUEUE) == 0 else QUEUE.pop(0))
    elif command[0] == 'empty':
        print( 1 if len(QUEUE) == 0 else 0 )
    else:
        # push
        QUEUE.append(command[1])
