# 2579 계단 오르기
# 🌟 뒤부터 차근차근 예시를 생각하면서 점화식 찾기!
import sys

N = int(sys.stdin.readline())
stair = []
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

point = [0] * N
for i in range(N):
    if i == 0:
        # 0번째 계단
        point[0] = stair[0]
    elif i == 1:
        # 0, 1번째 계단
        point[1] = stair[1] + point[0]
    elif i == 2:
        # 0, 2번째 계단 / 1, 2번째 계단 (점수가 없는 바닥에서 시작)
        point[2] = max(stair[0], stair[1]) + stair[2]
    # elif i == 3: 연속 3계단을 오르면 안됨 (1번, 3번 / 0번, 2번, 3번)
    #     point[3] = max(point[1] + stair[3], point[0] + stair[2] + stair[3])
    else:
        point[i] = max(point[i-2], point[i-3] + stair[i-1]) + stair[i]

print(point[-1])
