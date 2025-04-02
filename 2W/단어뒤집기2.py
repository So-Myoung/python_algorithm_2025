text = list(str(input()))
lists = []
mirror_flag = True

# print(text)

for i in text:

    if i == "<" and mirror_flag == True:
        lists.reverse()
        print(''.join(lists), end="")
        print('<', end="")

        mirror_flag = False
        lists = []

    elif i == ">" and mirror_flag == False:
        print(''.join(lists), end="",)
        print('>', end="")

        mirror_flag = True
        lists = []

    elif i == " " and mirror_flag == True:
        lists.reverse()
        print(''.join(lists), end=" ")

        lists = []

    elif i == " " and mirror_flag == False:
        print(''.join(lists), end=" ")

        lists = []

    else:
        lists.append(i)

if mirror_flag:
    lists.reverse()
    print(''.join(lists), end="")
else:
    print(''.join(lists), end="")