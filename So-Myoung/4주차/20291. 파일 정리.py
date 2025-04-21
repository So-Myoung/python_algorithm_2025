n = int(input())
dic = {}

for _ in range(n):
    fileName, fileType = input().split('.')

    if fileType in dic:
        dic[fileType] += 1
    else:
        dic[fileType] = 1

res = sorted(dic.items(), key=lambda x: x[0])

for name, n in res:
    print(name, n)