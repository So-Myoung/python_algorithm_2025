n = int(input())

def dp(n):
    dp = [i for i in range(n + 1)]
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(dp(n) % 10007)
    