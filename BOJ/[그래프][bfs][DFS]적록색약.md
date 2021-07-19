# 문제

```
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
```

# 풀이 방법

색약인 사람과 아닌사람의 지도를 2개 만들어 주었다.
bfs를 하면서 방문한 곳은 0으로 바꾸어 주었다.
따라서 0이 아닌 좌표를 시작점으로 돌되, 색약인 사람의 지도와 아닌사람의 지도, 이렇게 2번을 따로 돌아주었고
bfs함수로 몇번 들어갔는지가 영역이 몇개인가를 나눌 수 있는 포인트 이기때문에 들어갈 때마다 cnt를 +1씩 해주었다.
    

# 코드
```
from collections import deque

def bfs(area, a, b, color):
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0 ,0]

    q=deque()
    q.append((a, b))


    while q:
        y, x = q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and area[ny][nx] == color:
                area[ny][nx]=0
                q.append((ny, nx))

n = int(input())

non_color_blindness=[] #정상
color_blindness=[] #색맹

for i in range(n):
    l=input()
    tmp=[]
    tmp2=[]
    for j in l:
        tmp.append(j)
        if j =='G':
            j = 'R'
        tmp2.append(j)
    non_color_blindness.append(tmp)
    color_blindness.append(tmp2)

nbcnt=0
bcnt=0

for i in range(n):
    for j in range(n):
        if non_color_blindness[i][j] != 0:
            nbcnt += 1
            bfs(non_color_blindness, i, j, non_color_blindness[i][j])

        if color_blindness[i][j] != 0:
            bcnt += 1
            bfs(color_blindness, i, j, color_blindness[i][j])

print(nbcnt, bcnt)



```

# 출처
    https://www.acmicpc.net/problem/10026
