# 174143 단어뒤집기
# 코드 수정 필요
import sys

S = list(sys.stdin.readline().strip())

words = ''
string = []  # 태그 사이 문자
tag = ''  # 태그 속 문자
tagFlag = False
while S:
    popped = S.pop(0)
    if popped == '<':
        tagFlag = True
        tag += popped
        if string:  # 앞에 글자가 있으면
            string.reverse()
            words += ''.join(string)
            string = []
    elif popped == '>':
        tagFlag = False
        words += tag + popped
        tag = ''
    else:  # 문자일 때
        if tagFlag:  # 괄호 속일 때
            tag += popped
        else:
            if popped == ' ':  # 빈칸일 경우
                if string:
                    string.reverse()
                    words += ''.join(string)
                    string = []
                words += popped
            else:
                string.append(popped)

if string:
    string.reverse()
    words += ''.join(string)

print(words)
