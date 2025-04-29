import collections
import re

num = int(input())
lists = []

for i in range(num):
    text = str(input())
    split_text = text.rsplit('.', 1)[1]
    lists.append(split_text)

dicts = collections.Counter(lists)
sort_dicts = sorted(dicts.keys())

for i in sort_dicts:
    print(i, dicts[i])