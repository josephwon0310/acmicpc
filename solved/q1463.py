n = int(input())

dp = [10000 for _ in range(1000001)]

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    #print(i)
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[int(i/3)] + 1, dp[i])
    elif i % 2 == 0:
        dp[i] = min(dp[int(i/2)] + 1, dp[i])
        
print(dp[10])
