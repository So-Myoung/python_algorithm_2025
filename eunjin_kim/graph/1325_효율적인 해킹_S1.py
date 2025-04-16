'''#44
bfs + pypy3로 풀어야 통과되는 문제...

[1]알고리즘, 최악복잡도
dfs, 인접리스트(방향반대), 방문여부, O(v+e) = 1010000
=> 10000 * 1010000인 듯(...?)

[2]경계값, 히든테케
n 10000 1
m 100000 1
'''

import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x):
  visited[x] += 1
  for y in graph[x]:
    if not visited[y]:
      dfs(y) 

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

cnt = [0]*(n+1)
for x in range(1, n+1):
  visited = [0]*(n+1)
  dfs(x)
  cnt[x] = sum(visited)

max_cnt = max(cnt)
for i in range(1, n+1):
  if cnt[i] == max_cnt:
    print(i, end=' ')


