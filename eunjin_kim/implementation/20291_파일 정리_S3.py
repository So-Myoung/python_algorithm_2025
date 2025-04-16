'''#43
확장자별 개수
확장자 사전순

defaultdict를 정렬할 수 있나? -> yes
'''

import sys 
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
files = defaultdict(int)

for _ in range(n):
    name, file = input().rstrip().split('.')
    files[file] += 1

for file in sorted(files):
    print(file, files[file])
