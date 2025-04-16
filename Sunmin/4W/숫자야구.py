from itertools import permutations

lists = list(permutations([1,2,3,4,5,6,7,8,9], 3))

N = int(input())
question = [list(map(int, input().split())) for _ in range(N)]

for q in question:
    num, strike, ball = q
    num = list(str(num))
    temp = []

    for candidate in lists:
        candi = list(map(str, candidate))
        s = 0
        b = 0

        for i in range(3):
            if num[i] == candi[i]:
                s += 1
            elif num[i] in candi:
                b += 1

        if s == strike and b == ball:
            temp.append(candidate)

    lists = temp

print(len(lists))
