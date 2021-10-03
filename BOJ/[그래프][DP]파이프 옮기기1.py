# 시간초과가 난 풀이.... 답은 맞다. 하지만 파이썬으로는 이렇게 풀어서는 안된다.
'''
from collections import deque
import sys
input = sys.stdin.readline


def direct(lst1, lst2):
    if lst1[0] == lst2[0] and lst1[1] != lst2[1]:  # 가로
        return 0
    elif lst1[0] != lst2[0] and lst1[1] == lst2[1]:  # 세로
        return 1
    elif lst1[0] != lst2[0] and lst1[1] != lst2[1]:  # 대각선
        return 2


def possible(lst1, lst2, x, y):
    possible_direct = []
    if direct(lst1, lst2) == 0:  # 가로
        if y == N-1:
            if graph[y][x+1] == 0:
                possible_direct.append(0)

        elif x != N-1 and y != N-1:
            if graph[y][x+1] == 0:
                possible_direct.append(0)
            if graph[y][x+1] == 0 and graph[y+1][x] == 0 and graph[y+1][x+1] == 0:
                possible_direct.append(2)
    elif direct(lst1, lst2) == 1:  # 세로
        if x == N-1:
            if graph[y+1][x] == 0:
                possible_direct.append(1)
        elif x != N-1 and y != N-1:
            if graph[y+1][x] == 0:
                possible_direct.append(1)
            if graph[y+1][x] == 0 and graph[y][x+1] == 0 and graph[y+1][x+1] == 0:
                possible_direct.append(2)

    elif direct(lst1, lst2) == 2:  # 대각선
        if x == N-1 and y != N-1:
            if graph[y+1][x] == 0:
                possible_direct.append(1)

        elif x != N-1 and y == N-1:
            if graph[y][x+1] == 0:
                possible_direct.append(0)

        elif x != N-1 and y != N-1:
            if graph[y][x+1] == 0:
                possible_direct.append(0)
            if graph[y+1][x] == 0:
                possible_direct.append(1)
            if graph[y][x+1] == 0 and graph[y+1][x] == 0 and graph[y+1][x+1] == 0:
                possible_direct.append(2)
    return possible_direct


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

q = deque()
q.append([[0, 0], [0, 1]])
cnt = 0

while q:
    lst1, lst2 = q.popleft()

    x = max(lst1[1], lst2[1])
    y = max(lst1[0], lst2[0])
    if (direct(lst1, lst2) == 0 and (y != N-1 and x == N-1)) or (direct(lst1, lst2) == 1 and (y == N-1 and x != N-1)):
        continue
    if y == N-1 and x == N-1:
        cnt += 1
        continue

    tmp = possible(lst1, lst2, x, y)
    for i in tmp:
        if i == 0:
            q.append([[y, x], [y, x+1]])
        elif i == 1:
            q.append([[y, x], [y+1, x]])
        elif i == 2:
            q.append([[y, x], [y+1, x+1]])

print(cnt)
'''
# dp를 활용한 풀이

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 0가로 1세로 2대각선
dp = [[[0]*N for _ in range(N)] for _ in range(3)]

dp[0][0][1] = 1

for i in range(2, N):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]
for y in range(1, N):
    for x in range(1, N):
        if graph[y][x] == 0 and graph[y-1][x] == 0 and graph[y][x-1] == 0:
            dp[2][y][x] = dp[0][y-1][x-1] + dp[1][y-1][x-1] + dp[2][y-1][x-1]
        if graph[y][x] == 0:
            dp[0][y][x] = dp[0][y][x-1]+dp[2][y][x-1]
            dp[1][y][x] = dp[1][y-1][x]+dp[2][y-1][x]

answer = 0
for i in range(3):
    answer += dp[i][-1][-1]

print(answer)
