# from collections import deque

# x=int(input())
# answer=1000000
# cnt=0
# q=deque()
# q.append((x, cnt))

# while q:
#     x, cnt = q.popleft()
    
#     if x==1:
#         if answer>cnt:
#             answer=cnt
#     else:
#         if x%3==0 and cnt+1<answer:
#             q.append((x//3, cnt+1))
            
#         if x%2==0 and cnt+1<answer:
#             q.append((x//2, cnt+1))
#         if cnt+1<answer:
#             q.append((x-1, cnt+1))
    
# print(answer)
import sys
sys.setrecursionlimit(100000000)

n = int(input())

dp=[0 for _ in range(n+1)]
dp[2]=1
for i in range(3, n+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i//2]+1, dp[i])
    if i%3==0:
        dp[i]=min(dp[i//3]+1, dp[i])
    
print(dp[n])
