#29

import sys
input = sys.stdin.readline

n = int(input())
seq = input()

prev = seq[0]
cnt = 1

for i in range(1, n):
    if prev != seq[i]:
        prev = seq[i]
        cnt += 1

print(cnt // 2 + 1)