# 문제

```
문제
인제대학교 생화학연구실에 재직중인 석교수는 전류가 침투(percolate) 할 수 있는 섬유 물질을 개발하고 있다. 이 섬유 물질은 2차원 M × N 격자로 표현될 수 있다. 편의상 2차원 격자의 위쪽을 바깥쪽(outer side), 아래쪽을 안쪽(inner side)라고 생각하기로 한다. 또한 각 격자는 검은색 아니면 흰색인데, 검은색은 전류를 차단하는 물질임을 뜻하고 흰색은 전류가 통할 수 있는 물질임을 뜻한다. 전류는 섬유 물질의 가장 바깥쪽 흰색 격자들에 공급되고, 이후에는 상하좌우로 인접한 흰색 격자들로 전달될 수 있다.

김 교수가 개발한 섬유 물질을 나타내는 정보가 2차원 격자 형태로 주어질 때, 바깥쪽에서 흘려 준 전류가 안쪽까지 침투될 수 있는지 아닌지를 판단하는 프로그램을 작성하시오.

	
(a) The current percolates.	(b) The current does not percolate.
예를 들어, Figure 1(a) 에서는 바깥쪽에서 공급된 전류가 안쪽까지 침투하지만, Figure 1(b)에서는 그렇지 못한다.

입력
첫째 줄에는 격자의 크기를 나타내는  M (2 ≤ M ≤ 1,000) 과 N (2 ≤ N ≤ 1,000) 이 주어진다. M줄에 걸쳐서, N개의 0 또는 1 이 공백 없이 주어진다. 0은 전류가 잘 통하는 흰색, 1은 전류가 통하지 않는 검은색 격자임을 뜻한다.

출력
바깥에서 흘려준 전류가 안쪽까지 잘 전달되면 YES를 출력한다.

그렇지 않으면 NO를 출력한다.


```

# 풀이 방법

이 문제는 첫째 줄의 0이 마지막 줄의 0까지 이어질 수 있는가를 묻는 문제이다.
따라서 bfs의 시작점을 첫번째 줄의 0의 좌표로 해주었다. 
그리고 탐색이 종료되었을 때 마지막 행의 좌표가 나온다면 'YES'를 출력해주고 아니라면 'NO'를 출력시켜 주었다.

    

# 코드
```
from collections import deque
m, n = map(int, input().split())

fiber = []
answer=''

for i in range(m):
    l=input()
    tmp=[]
    for j in l:
        tmp.append(int(j))
    fiber.append(tmp)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

q=deque()

for i in range(n):
    if fiber[0][i] == 0:
        q.append((0,i))
        fiber[0][i]=1
        while q:
            y, x = q.popleft()

            if y == m-1:
                answer='YES'
                break
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<n and 0<=ny<m and fiber[ny][nx]==0:
                    q.append((ny, nx))
                    fiber[ny][nx] = 1
            
if answer != 'YES':
    answer='NO'
print(answer)

```

# 출처
    https://www.acmicpc.net/problem/13565
