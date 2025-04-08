n = int(input())

# dp[i][j]: i번째 계단까지 올라 섰을 때 점수 합의 최댓 값, j개의 계단을 연속해서 밟음
# 1 index base
dp = [[0] * 3 for _ in range(301)]
score = [0] + [int(input()) for _ in range(n)]

# dp 초기값
if n > 1:
    dp[1][1] = score[1]
    dp[1][2] = 0
    dp[2][1] = score[2]
    dp[2][2] = score[1] + score[2]

for i in range(3, n+1):
    # 점화식
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + score[i]
    dp[i][2] = dp[i-1][1] + score[i]

print(score[1] if n == 1 else max(dp[n][1], dp[n][2]))