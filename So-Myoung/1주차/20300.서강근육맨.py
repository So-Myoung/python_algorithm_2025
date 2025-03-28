n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = []

if n % 2 == 1:
    res.append(arr.pop())
for i in range(len(arr) // 2):
    res.append(arr[i] + arr[len(arr) - 1 - i])

print(max(res))