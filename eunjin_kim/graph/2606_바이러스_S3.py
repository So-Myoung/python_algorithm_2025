import sys
input = sys.stdin.readline


def dfs(x):
    visited[x] = 1

    for y in graph[x]:
        if visited[y] == 0:
            dfs(y)


n = int(input())
c = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(c):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(sum(visited) - 1)

