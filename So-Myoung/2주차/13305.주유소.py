n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_price = prices[0]
res = []

for i, p in enumerate(prices[:-1]):
    min_price = min(p, min_price)
    res.append(distances[i] * min_price)

print(sum(res))