from collections import deque, defaultdict

N = int(input())
M = int(input())
edges = [tuple(map(int, input().split())) for _ in range(M)]

neighbors = defaultdict(list)
for edge in edges:
    a, b = edge
    neighbors[a].append(b)
    neighbors[b].append(a)


# bfs
queue = deque([1])
visited = set()
visited.add(1)
count = 0

while queue:
    node = queue.popleft()
    for neighbor in neighbors[node]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)
            visited.add(neighbor)
            count += 1

print(count)
