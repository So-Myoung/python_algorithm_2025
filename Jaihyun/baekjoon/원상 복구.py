from collections import defaultdict

n,k = map(int,input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))


# union find 로 풀어보자
def union_find(step, i):
    index = d[i]
    for j in range(step):
        index = d[index]
        if index == i:
            
            break
    return index



visited = set()
for i in range(n):
    union_find(k-1, i)
