import copy

a, b = map(int, input().split())
result = list(map(int, input().split()))
sequence = list(map(int, input().split()))
sequence = [x - 1 for x in sequence]
temp = []

for _ in range(b):
    temp = [0] * a

    for i in range(len(sequence)):
        # temp[i] = result[sequence[i]]
        temp[sequence[i]] = result[i]

    result = temp

print(*result)

# 5 2
# 4 1 3 5 2
# 4 3 1 2 5
