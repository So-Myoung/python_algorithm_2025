import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

before = 1_000_000_000 
cost = 0

for i in range(n-1):
  if city[i] < before:
    before = city[i]
  
  cost += before * road[i]

print(cost)
    
