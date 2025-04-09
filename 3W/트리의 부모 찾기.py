import sys
from collections import deque

sys.setrecursionlimit(100000)

num = int(input())
node = [[] for _ in range(num + 1)]

for _ in range(num - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

print("node", node)

DFS_visited = [0] * (num + 1)
def DFS(V):
    for i in node[V]:
        if DFS_visited[i] == 0:
            DFS_visited[i] = V
            DFS(i)


DFS(1)
print(DFS_visited)

# queue = deque()
#
# def BFS():
#     visited = [0] * (num + 1)
#     parent = [0] * (num + 1)
#     BFS_ans = []
#     queue.append(1)
#     visited[1] = 1
#
#
#     while queue:
#         now = queue.popleft()
#
#         for i in node[now]:
#             if visited[i] == 0:
#                 queue.append(i)
#                 parent[i] = now
#                 BFS_ans.append(now)
#                 visited[i] = 1
#
#     print(parent)
#
#
#
# BFS()
