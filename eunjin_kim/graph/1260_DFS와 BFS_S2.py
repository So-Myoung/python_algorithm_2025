from collections import deque
import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = 1
    answer.append(x)
    for i in range(m):
        if x in graph[i] :
            y = graph[i][0] if x == graph[i][1] else graph[i][1]
            if not visited[y]:
                dfs(y)



def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        x = queue.popleft()
        answer.append(x)
        for i in range(m):
            if x in graph[i] :
                y = graph[i][0] if x == graph[i][1] else graph[i][1]
                if not visited[y]:
                    queue.append(y)
                    visited[y] = 1

n, m, v = map(int, input().split())
graph = []
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph.append(sorted([n1, n2]))
graph = sorted(graph, key = lambda x : (x[0], x[1]))

answer = []
visited = [0] * (n+1)
dfs(v)
print(*answer)

answer = []
visited = [0] * (n+1)
bfs(v)
print(*answer)
