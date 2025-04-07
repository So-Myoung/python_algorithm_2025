# 그래프 탐색 - 11725 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
nodes = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

result = [0] * (N+1)


def dfs(start):
    for i in nodes[start]:
        if not result[i]:
            result[i] = start
            dfs(i)


dfs(1)
for i in range(2, N+1):
    print(result[i])
