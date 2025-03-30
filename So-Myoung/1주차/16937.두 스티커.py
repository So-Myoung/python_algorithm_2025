h, w = map(int, input().split())
n = int(input())
stk = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(i+1, n):
        r1, c1 = stk[i]
        r2, c2 = stk[j]

        # 두 스티커 모두 회전하지 않는 경우(세로로 나란히 배치/가로로 나란히 배치)
        if (r1 + r2 <= h and max(c1, c2) <= w) or (c1 + c2 <= w and max(r1, r2) <= h):
            res = max(res, r1*c1 + r2*c2)
        # 첫 번째 스티커만 회전하는 경우
        if (c1 + r2 <= h and max(r1, c2) <= w) or (r1 + c2 <= w and max(c1, r2) <= h):
            res = max(res, r1*c1 + r2*c2)
        # 두 번째 스티커만 회전하는 경우
        if (r1 + c2 <= h and max(c1, r2) <= w) or (c1 + r2 <= w and max(r1, c2) <= h):
            res = max(res, r1*c1 + r2*c2)
        # 두 스티커 모두 회전하는 경우
        if (c1 + c2 <= h and max(r1, r2) <= w) or (r1 + r2 <= w and max(c1, c2) <= h):
            res = max(res, r1*c1 + r2*c2)

print(res)