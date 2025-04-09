from collections import Counter
from itertools import combinations

name = list(str(input()))
num = int(input())
visted = [0] * num
price = []
book_name = []
total_price = 0


for i in range(num):
    a, b = input().split()
    a = int(a)
    price.append(a)
    book_name.append(list(str(b)))

target_count = Counter(name)
min_cost = float('inf')


for i in range(1, num + 1):
    for combination in combinations(range(num), i):
        current_count = Counter()
        total_price = 0

        for idx in combination:
            visted[idx] = 1
            current_count.update(book_name[idx])
            total_price += price[idx]
        can_make = True
        for char in target_count:
            if current_count[char] < target_count[char]:
                can_make = False
                break

        if can_make:
            min_cost = min(min_cost, total_price)


        for idx in combination:
            visted[idx] = 0

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
