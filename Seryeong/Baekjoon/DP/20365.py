# DP - 11726 2xn 타일링
import sys

N = int(sys.stdin.readline())

DP = [0] * (N + 1)

if N <= 2:
    print(N)
else:
    DP[1] = 1
    DP[2] = 2
    for i in range(3, N+1):  # 인덱스 확인
        DP[i] = (DP[i-1] + DP[i-2]) % 10007
    print(DP[N])
