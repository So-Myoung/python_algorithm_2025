from collections import deque

computer, node = map(int, input().split())
lists = [[] for i in range(computer + 1)]

for _ in range(node):
    a, b = map(int, input().split())
    lists[b].append(a)

# print(lists)


def BFS(num):
    visited = [False] * (computer + 1)
    visited[num] = True
    queue = deque()
    queue.append(num)
    ans = 0

    while queue:

        now = queue.popleft()

        for i in lists[now]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                ans += 1

    ans_lists.append(ans)


ans_lists = []

for i in range(computer+1):
    BFS(i)

# print(ans_lists)
max_num = max(ans_lists)

for i in range(len(lists)):
    if ans_lists[i] == max_num:
        print(i,end=" ")
