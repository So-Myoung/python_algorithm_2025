# 1463 1로 만들기
import sys
N = int(sys.stdin.readline())

if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
else:
    DP = [0] * (N + 1)
    DP[1] = 0
    DP[2] = 1
    DP[3] = 1
    for i in range(4, N+1):
        DP[i] = DP[i-1] + 1
        if i % 3 == 0:
            # 3을 나누는 연산을 더한 것 vs 1을 빼는 연산을 더한 것
            DP[i] = min(DP[i//3] + 1, DP[i])
        if i % 2 == 0:
            # 2을 나누는 연산을 더한 것 vs 1을 빼는 연산을 더한 것
            DP[i] = min(DP[i//2] + 1, DP[i])

    print(DP[N])
