n = int(input())

# dp = 1로 만들기 위한 최소 연산 횟수
# 가능한 연산은 3가지
# 1. dp[i] = dp[i-1] + 1
# 2. dp[i//2] + 1
# 3. dp[i//3] + 1
# 근데 나눠지는지 미리 체크해줘야됨

dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])