# 1913 달팽이
import sys
N = int(sys.stdin.readline())
numToFind = int(sys.stdin.readline())

table = [[0] * N for _ in range(N)]

x = N//2
y = N//2
num = 2
move = 1
table[y][x] = 1
xToFind = x
yToFind = y

# for문으로 방향을 조정해서 하는 더 간댠한 방법이 있음
while num <= N * N and 0 <= x <= N and 0 <= y <= N:
    for _ in range(move):
        y -= 1
        table[y][x] = num
        if num == numToFind:
            yToFind = y
            xToFind = x
        num += 1
    if y < 0:
        break
    for _ in range(move):
        x += 1
        table[y][x] = num
        if num == numToFind:
            yToFind = y
            xToFind = x
        num += 1
    if x > N:
        break
    move += 1
    for _ in range(move):
        y += 1
        table[y][x] = num
        if num == numToFind:
            yToFind = y
            xToFind = x
        num += 1
    if y > N:
        break
    for _ in range(move):
        x -= 1
        table[y][x] = num
        if num == numToFind:
            yToFind = y
            xToFind = x
        num += 1
    if x < 0:
        break
    move += 1

for i in table:
    for j in i:
        print(j, end=' ')
    print()

print(yToFind + 1, xToFind + 1)
