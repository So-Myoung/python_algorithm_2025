#42
'''
100!/6!94!
100 99 98 ... 6번, 나누기 6!
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = n
divide = m

for i in range(1, m):
    n -= 1
    res *= n
    divide *= i

print(res//divide)

