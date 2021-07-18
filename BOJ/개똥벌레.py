
import sys

input = sys.stdin.readline

n, h = map(int, input().split())

sector=[[0 for _ in range(n)] for _ in range(h)]

obs=[int(input()) for _ in range(n)]

cnt_obs=[]

answer=0
cnt=0

for i in range(n):
    if i % 2 == 0:
        for j in range(0, obs[i]):
            sector[j][i] = 1
    else:
        for j in range(h-obs[i], h):
            sector[j][i] = 1

for i in sector:
    cnt_obs.append(sum(i))
answer = min(cnt_obs)
for i in cnt_obs:
    if i == answer:
        cnt+=1

print(answer, cnt)