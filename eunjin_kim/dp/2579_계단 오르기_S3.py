import sys
input = sys.stdin.readline

n = int(input())
steps = [int(input()) for _ in range(n)]
dp = [0] * n


def solution():
    if n == 1:
        return steps[0]
    if n == 2:
        return steps[0] + steps[1]
    
    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1]
    
    for i in range(2, n):
        dp[i] = max(steps[i] + steps[i-1] + dp[i-3], 
                    steps[i] + dp[i-2])
    
    return dp[-1]


print(solution())




