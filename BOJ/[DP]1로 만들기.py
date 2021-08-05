n = int(input())

dp = [0]*(n+1)
dp[1] = 0


for i in range(2, n+1):
    if i % 6 == 0:
        dp[i] = 1 + min(dp[i-1], dp[i//2], dp[i//3])
    elif i % 2 == 0:
        dp[i] = 1 + min(dp[i-1], dp[i//2])
    elif i % 3 == 0:
        dp[i] = 1 + min(dp[i-1], dp[i//3])
    else:
        dp[i] = 1 + dp[i-1]
print(dp[n])
