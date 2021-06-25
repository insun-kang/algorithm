# 문제

```
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
```

# 풀이 방법

체스판의 크기를 받고 나이트가 움직일 수 있는 x, y 값들을 받아주어 bfs를 돌렸다.
bfs함수에 시작점과 끝점을 넣어서 끝점에 도착할 시에 cnt를 리턴하도록 만들어주었다.
    

# 코드
```
from collections import deque

def bfs(a1, b1, a2, b2):
    dx=[2, 1, -2, -1, 1, 2, -1, -2]
    dy=[1, 2, 1, 2, -2, -1, -2, -1]
    
    answer=[]
    cnt = 0

    q=deque()

    q.append((b1, a1, cnt))
    chess_map[b1][a1]=1

    while q:

        y, x, cnt = q.popleft()

        if y == b2 and x == a2:
            return cnt

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<l and 0<=ny<l and chess_map[ny][nx] == 0:
                q.append((ny, nx, cnt+1))
                chess_map[ny][nx] = 1

    # return answer

n = int(input())

for i in range(n):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    chess_map = [[0 for _ in range(l)] for _ in range(l)]


    print(bfs(y1, x1, y2, x2))




```

# 출처
    https://www.acmicpc.net/problem/7562
