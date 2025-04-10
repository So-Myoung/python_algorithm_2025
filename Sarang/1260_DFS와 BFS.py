import sys
from collections import deque


n, m, v = map(int, sys.stdin.readline().split())

answer_dfs = []
answer_bfs = []
graph = [[] for i in range(n+1)]
dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)


def dfs(node):
    dfs_visited[node] = 1
    answer_dfs.append(node)
    for i in graph[node]:
        if dfs_visited[i] == 0:
            dfs(i)
    return


def bfs(node):
    queue = deque()
    queue.append(node)
    bfs_visited[node] = 1
    answer_bfs.append(node)
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            if bfs_visited[i] == 0:
                bfs_visited[i] = 1
                queue.append(i)
                answer_bfs.append(i)
    return


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

for i in graph:
    i.sort()

dfs(v)
bfs(v)

print(' '.join(map(str, answer_dfs)))
print(' '.join(map(str, answer_bfs)))
