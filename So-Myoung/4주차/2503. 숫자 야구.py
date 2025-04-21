from itertools import permutations


n = int(input())
num_list = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
q = []
res = 0

for _ in range(n):
    n, s, b = input().split()
    q.append([n, int(s), int(b)])

for per in num_list:
    is_possible = True

    for q_num, q_s, q_b in q:
        s, b = 0, 0
        for i in range(3):
            if str(per[i]) == q_num[i]:
                s += 1
            elif str(per[i]) in q_num:
                b += 1
        if s != q_s or b != q_b:
            is_possible = False
            break

    if is_possible:
        res += 1

print(res)