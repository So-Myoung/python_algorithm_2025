# 아래처럼 풀었더니 타임 초과..
# 100C6 이면 조합이 11억개
# from itertools import combinations
#
# n, m = map(int, input().split())
#
# n_list = list(combinations([i for i in range(1, n+1)], m))
# print(len(n_list))


# dp 보다 math로 푸는게 유리. 조합 전체 테이블 만들 필요 X
import math

n, m = map(int, input().split())
print(math.comb(n, m))


# 굳이 점화식으로 풀자면
# 조합 점화식 : n-1Cr-1 + n-1Cr
# D[i][j] = D[i - 1][j] + D[i - 1][j - 1]