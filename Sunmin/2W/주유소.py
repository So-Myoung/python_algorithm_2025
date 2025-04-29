num = int(input())
distances = list(map(int, input().split()))  # 길이
prices = list(map(int, input().split()))  # 리터당 가격
total_cost = 0  # 총 비용
min_price = prices[0]

for i in range(0, num - 1):
    if min_price > prices[i]:
        min_price = prices[i]

    total_cost += min_price * distances[i]

print(total_cost)