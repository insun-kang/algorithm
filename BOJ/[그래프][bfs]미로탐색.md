# 문제

```
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
```

# 풀이 방법

먼저 미로의 형태를 만들어서 저장시켜주었다.
그리고 각 단계별로 같은 값을 가지기 위해서 deque에 좌표와 cnt값을 넣어주었고 bfs를 이용해서 해결했다.
    

# 코드
```
from collections import deque

n, m = map(int, input().split())
miro = []
for i in range(n):
    l=input()
    tmp=[]
    for j in l:
        tmp.append(int(j))
    miro.append(tmp)
    
dx=[1,0,-1,0]
dy=[0,1,0,-1]

cnt=1

q=deque()

q.append((0,0,cnt))
miro[0][0]=0
while q:
    x, y, cnt = q.popleft()
    if x==n-1 and y ==m-1:
        print(cnt)
        break

    cnt += 1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<m and miro[nx][ny]==1:
            q.append((nx, ny, cnt))
            miro[nx][ny]=0

```

# 출처
    https://www.acmicpc.net/problem/2178
