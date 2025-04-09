from collections import deque

N, M, V = map(int, input().split())

lists = [[] for _ in range(N + 1)]
queue = deque()

for _ in range(M):
    s, e = map(int, input().split())
    lists[s].append(e)
    lists[e].append(s)

for i in range(1, N + 1):
    lists[i].sort()


def BFS():
    visited = [0] * (N + 1)
    BFS_ans = []
    BFS_ans.append(V)
    queue.append(V)
    visited[V] = 1

    while queue:
        now = queue.popleft()

        for i in lists[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                BFS_ans.append(i)

    print(*BFS_ans)


DFS_visited = [0] * (N + 1)
DFS_ans = []


def DFS(V, DFS_visited, lists):
    DFS_visited[V] = 1
    DFS_ans.append(V)

    for i in lists[V]:
        if not DFS_visited[i] == 1:
            V = i
            DFS(V, DFS_visited, lists)


DFS(V, DFS_visited, lists)
print(*DFS_ans)
BFS()

