from collections import defaultdict


def dfs(graph, visited, node):
    visited[node] = True
    count = 1

    for v in graph[node]:
        if not visited[v]:
            count += dfs(graph, visited, v)

    return count


n = int(input())
connected = int(input())
graph = defaultdict(list)

for _ in range(connected):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

visited = [False] * (n + 1)
print(dfs(graph, visited, 1) - 1)  # 1번 컴퓨터 제외
