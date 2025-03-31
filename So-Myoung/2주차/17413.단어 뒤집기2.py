s = input()
in_tag = False
res = []
temp_word = ''

for c in s:
    if c == '<':
        if temp_word:
            res.append(temp_word[::-1])
            temp_word = ''
        res.append(c)
        in_tag = True
    elif c == '>':
        res.append(c)
        in_tag = False
    elif in_tag:
        res.append(c)
    elif not in_tag:
        if c == ' ':
            if temp_word:
                res.append(temp_word[::-1])
                temp_word = ''
            res.append(c)
        else:
            temp_word += c

if temp_word:
    res.append(temp_word[::-1])

print(''.join(res))