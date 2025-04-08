from collections import defaultdict, deque


def dfs(graph, visited, node):
    visited[node] = True
    print(node, end=' ')

    for n in graph[node]:
        if not visited[n]:
            dfs(graph, visited, n)


def bfs(graph, visited, node):
    visited[node] = True
    queue = deque([node])

    while queue:
        n = queue.popleft()
        print(n, end=' ')

        for n in graph[n]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)


n, m, v = map(int, input().split())
graph = defaultdict(list)
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 노드부터 방문하므로 오름차순 정렬
for key in graph:
    graph[key].sort()

dfs(graph, dfs_visited, v)
print()
bfs(graph, bfs_visited, v)
