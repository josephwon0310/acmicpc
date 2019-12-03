from time import time


n = int(input())

def tile(n):
    dp = [-1 for _ in range(1001)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 10007

start = time()
print(tile(n))
print(time()- start)

def tile_recur(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return tile_recur(n-1) + tile_recur(n-2)


start = time()
print(tile_recur(n))
print(time() - start)
