num = int(input())
lists = list(str(input()))
B_set = 0
R_set = 0

for i in range(len(lists)):
    # print(i, len(lists))

    if i == len(lists) - 1:
        if lists[i] == 'R' and lists[i - 1] == 'B':
            R_set += 1
            
            # print("B-----", R_set)
            break
        elif lists[i] == 'B' and lists[i - 1] == 'R':
            B_set += 1
            # print("R-----", R_set)
            break
        elif lists[i] == 'B' and lists[i - 1] == 'B':
            B_set += 1
            # print("R-----", R_set)
            break
        elif lists[i] == 'R' and lists[i - 1] == 'R':
            R_set += 1
            # print("R-----", R_set)
            break

    if lists[i] == 'B' and lists[i + 1] == 'R':
        B_set += 1
    elif lists[i] == 'R' and lists[i + 1] == 'B':
        R_set += 1

#     print(lists[i])
#     print('B=', B_set, ' R=', R_set)
# print('B=', B_set, ' R=', R_set)
print(min(B_set, R_set) + 1)
