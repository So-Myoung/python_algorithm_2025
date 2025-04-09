#31

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(k):
    seq = [0] * n
    for i in range(n):
        seq[d[i]-1] = s[i]
    s = seq

print(*seq)

    
