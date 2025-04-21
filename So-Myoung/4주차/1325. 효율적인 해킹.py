from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])
    count = 1

    while queue:
        node = queue.popleft()

        for connected in graph[node]:
            if not visited[connected]:
                visited[connected] = True
                count += 1
                queue.append(connected)

    return count


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
max_count = 0
res = []

for _ in range(m):
    a, b = map(int, input().split())
    # A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다(단방향, B->A)
    graph[b].append(a)

for i in range(1, n + 1):
    cur = bfs(i)
    if cur > max_count:
        max_count = cur
        res = [i]
    elif cur == max_count:
        res.append(i)

print(*res)