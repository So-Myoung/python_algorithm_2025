num = int(input())
ans = 0

lists = [0] * (50000)

for i in range(1, 223):
    lists[i ** 2] = 1

for i in range(1, num + 1):
    if lists[i] == 0:
        min_value = 10

        for j in range(1, int(i ** 0.5) + 1):
            min_value = min(min_value, lists[i - j ** 2] + 1)
        lists[i] = min_value


print(lists[num])