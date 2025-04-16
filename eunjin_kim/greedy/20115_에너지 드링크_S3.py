import sys
input = sys.stdin.readline

n = int(input())
seq = sorted(map(int, input().split()), reverse=True)
print(seq[0] + sum(seq[1:])/2)