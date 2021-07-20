from collections import deque

def solution(n):
    ans=[]
    cnt=0
    while True:
        if n%2==1:
            n=n-1
            cnt+=1
        else:
            n=n//2
        if n==0:
            return cnt
    
# def solution(n):
#     ans=[]
#     q=deque()
#     q.append([0,0])
#     while q:
#         x, cnt=q.popleft()
#         if x==n:
#             ans.append(cnt)
        
#         if x+1<n:
#             q.append([x+1, cnt+1])
#         elif x+1==n:
#             ans.append(cnt+1)
#         if 2*x<=n and 2*x != 0 :
#             q.append([2*x, cnt])
#         elif 2*x==n:
#             ans.append(cnt)

#     return min(ans)