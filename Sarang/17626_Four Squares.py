# 브루트포스
import sys
import math


n = int(sys.stdin.readline())

# 제곱수 체크
def is_square(num):
    if math.sqrt(num) == int(math.sqrt(num)):
        return True
    else:
        return False

min_v = 4   # 최대 개수가 4개

# 하나의 제곱수의 합인 경우 (n 자체가 제곱수)
if is_square(n):
    min_v = 1
else:
    for i in range(int(math.sqrt(n)), 0, -1):   # 숫자 n의 제곱근부터 1까지 역순으로 반복
        # 두 제곱수의 합인 경우
        if is_square(n-(i**2)):
            min_v = 2
            break
        else:
            for j in range(int(math.sqrt(n-i**2)), 0, -1):
                # 세 제곱수의 합인 경우
                if is_square(n-(i**2)-(j**2)):
                    min_v = 3
                    break
print(min_v)



'''
# DP - Python3 시간초과
import sys
import math


n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[1] = 1   # 1 = 1^2 -> 1개

for i in range(2, n+1):
    min_v = 1e9
    for j in range(1, int(math.sqrt(i))+1):
        # i보다 작은 제곱수(j**2)를 뺀 나머지 값에 대한 최소 제곱수 개수 + 1
        min_v = min(min_v, dp[i-j**2])
    dp[i] = min_v + 1   # +1은 현재 사용한 제곱수 j²를 추가한 것
print(dp[n])

'''
