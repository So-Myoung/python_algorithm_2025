from collections import deque
def dfs(graph, visited, V, res):
    visited[V] = True
    res.append(V)

    for i in graph[V]:
        if not visited[i]:
            dfs(graph, visited, i, res)
    
    return res

def bfs(graph, visited, V, res):
    visited[V] = True
    q = deque([V])

    while q:
        now = q.popleft()
        res.append(now)
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    
    return res

N, M, V = map(int, input().split())
graph = {i:[] for i in range(N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

res = []
visited = [False] * (N+1)
dfs(graph, visited, V, res)
print(*res)

res = []
visited = [False] * (N+1)
bfs(graph, visited, V, res)
print(*res)