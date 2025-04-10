n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    min_val = float('inf')
    j = 1
    while j * j <= i:
        min_val = min(min_val, dp[i - j * j])
        j += 1
    dp[i] = min_val + 1

print(dp[n])