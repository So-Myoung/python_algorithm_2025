import sys
input = sys.stdin.readline

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
i = 0

n = int(input())
target = int(input())
target_idx = [0, 0]

graph = list([0 for _ in range(n)] for _ in range(n))
x, y = int(n/2), int(n/2)
graph[x][y] = 1

num = 1


def snail():
    global num, x, y, i  # 전역변수를 수정하는 경우

    for _ in range(cnt):
        if num == target:  # 타겟넘버 찾기
            target_idx[0], target_idx[1] = x + 1, y + 1
        if num == n ** 2:  # 종료조건
            return True

        num += 1
        dx, dy = d[i]
        x, y = x + dx, y + dy
        graph[x][y] = num

    i = (i + 1) % 4


cnt = 1
while True:
    if snail():
        break

    snail()
    cnt += 1


for _ in range(n):
    print(*graph[_])

print(*target_idx)


