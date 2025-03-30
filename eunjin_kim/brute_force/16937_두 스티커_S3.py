# 스파게티... 첫번째 스티커는 무조건 붙일 수 있다고 가정한 것이 패착이었다.
# 첫번째 스티커는 고정, 두번째 스티커를 x 혹은 y축 방향으로 이동, 두번째 스티커 90도 회전여부, 모눈종이 90도 회전여부 (경우의 수 2*2*2 = 8가지)

import sys
input = sys.stdin.readline


h, w = map(int, input().split())
n = int(input())

stickers = []
for i in range(n):
    r, c = map(int, input().split())
    stickers.append([r, c])


def possible_stickers(one, two):
    area = one[0] * one[1] + two[0] * two[1]

    for j in range(one[1]):
        height1 = one[0] + two[0]
        width1 = j + two[1]

        if height1 <= h and width1 <= w and one[0] <= h and one[1] <= w:  # 1
            return area
        if height1 <= w and width1 <= h and one[0] <= w and one[1] <= h:  # 2
            return area

        height2 = one[0] + two[1]
        width2 = j + two[0]

        if height2 <= h and width2 <= w and one[0] <= h and one[1] <= w:  # 3
            return area
        if height2 <= w and width2 <= h and one[0] <= w and one[1] <= h:  # 4
            return area

    for i in range(one[0]):
        height1 = i + two[0]
        width1 = one[1] + two[1]

        if height1 <= h and width1 <= w and one[0] <= h and one[1] <= w:  # 5
            return area
        if height1 <= w and width1 <= h and one[0] <= w and one[1] <= h:  # 6
            return area

        height2 = i + two[1]
        width2 = one[1] + two[0]

        if height2 <= h and width2 <= w and one[0] <= h and one[1] <= w:  # 7
            return area
        if height2 <= w and width2 <= h and one[0] <= w and one[1] <= h:  # 8
            return area

    return 0


max_area = 0

for i in range(n-1):
    for j in range(i+1, n):
        area = possible_stickers(stickers[i], stickers[j])
        max_area = max(max_area, area)

print(max_area)
