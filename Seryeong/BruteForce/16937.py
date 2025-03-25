# 두 스티커
import sys
from itertools import combinations

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
stickers = []
for _ in range(N):
    R, C = map(int, sys.stdin.readline().split())
    stickers.append([R, C, R * C])

combi = list(combinations(stickers, 2))
maxWidth = 0
for sticker in combi:
    a = sticker[0]
    b = sticker[1]

    # 한 변이 모눈종이를 벗어나면
    if (a[0] > H or a[0] > W) and (a[1] > H or a[1] > W):
        continue
    if (b[0] > H or b[0] > W) and (b[1] > H or b[1] > W):
        continue
    print('====')
    print(a[0]+b[0], a[1]+b[1], a[0]+b[1], a[1]+b[0])
    # 🚨 두 개의 스티커를 붙였을 때 모눈종이를 벗어나면

    print(a, b)
    width = a[2] + b[2]
    if H * W >= width > maxWidth:
        maxWidth = width  # 최댓값 업데이트

print(maxWidth)
