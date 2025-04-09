num = int(input())

if num <= 5:
    lists = [0] * 6
    lists[1] = 1
    lists[2] = 2
    lists[3] = 3
    lists[4] = 5
    lists[5] = 8
    print(lists[num])
    quit()

lists = [0] * (num + 1)

lists[1] = 2
lists[2] = 2
lists[3] = 3
lists[4] = 5
lists[5] = 8

for i in range(6, num + 1):
    lists[i] = lists[i - 1] + lists[i - 2]

# print(lists)
print(lists[num] % 10007)
