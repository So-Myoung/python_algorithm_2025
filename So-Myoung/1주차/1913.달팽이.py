n = int(input())
target = int(input())

arr = [[0] * n for _ in range(n)]

# 규칙 상 -> 우 -> 하 -> 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = n//2, n//2
arr[x][y] = 1
target_x, target_y = x + 1, y + 1
num = 2 # 다음 채울 숫자
move_count = 1 # 이동 횟수
i = 0 # dx,dy index

# 규칙: 상(1) → 우(1) → 하(2) → 좌(2) → 상(3) → 우(3) → 하(4) → 좌(4) ...
while num <= n * n:
    for _ in range(2):
        for _ in range(move_count):
            x, y = x+dx[i], y+dy[i]

            if (0 <= x < n) and (0 <= y < n):
                arr[x][y] = num
                if num == target:
                    target_x, target_y = x + 1, y + 1
                num += 1

        i = (i + 1) % 4

    move_count += 1

for row in arr:
    print(*row)

print(target_x, target_y)