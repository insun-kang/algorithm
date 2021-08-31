from bisect import bisect_left

N = int(input())

children = [int(input()) for _ in range(N)]

dp = []

for i in children:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i

print(len(children) - len(dp))
