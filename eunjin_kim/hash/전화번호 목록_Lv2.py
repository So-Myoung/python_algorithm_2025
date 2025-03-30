from collections import defaultdict


def solution(phone_book):
    phone_dict = defaultdict(int)

    for phone in phone_book:
        phone_dict[phone] = 1

    for phone in phone_book:
        for i in range(len(phone)):
            if phone_dict[phone[:i]]:
                return False

    return True
