text = input()

result = ""
in_tag = False
stack = []
temp = ""

for char in text:
    if char == '<':
        in_tag = True
        while stack:
            result += stack.pop()
    if in_tag:
        temp += char
        if char == '>':
            in_tag = False
            result += temp
            temp = ""
    else:
        if char != ' ':
            stack.append(char)
        else:
            while stack:
                result += stack.pop()
            result += ' '

# 마지막 단어 처리
while stack:
    result += stack.pop()

print(result)
