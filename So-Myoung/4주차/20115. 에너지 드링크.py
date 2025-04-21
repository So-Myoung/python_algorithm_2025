# 임의의 서로 다른 두 에너지 드링크를 고른다
# 더 적은 양의 드링크의 반을 버려야 에너지 드링크 양이 최대

from collections import deque

n = int(input())
drinks = list(map(int, input().split()))

drinks.sort()
queue = deque(drinks)
res = queue.pop()

while queue:
    res += queue.popleft() / 2

print(res)