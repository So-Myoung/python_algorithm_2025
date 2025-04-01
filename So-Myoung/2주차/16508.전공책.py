def dfs(i, current_price, current_book):
    global min_price, is_possible

    temp = list(t)
    for c in current_book:
        if c in temp:
            temp.remove(c)

    if not temp:
        min_price = min(min_price, current_price)
        is_possible = True
        return

    if i == n:
        return

    # 책 선택 0
    dfs(i + 1, current_price + books[i][0], current_book + books[i][1])
    # 책 선택 X
    dfs(i + 1, current_price, current_book)


t = input()
n = int(input())
books = []

for _ in range(n):
    price, book = input().split()
    books.append((int(price), book))

min_price = float('inf')
is_possible = False

dfs(0, 0, "")
print(min_price if is_possible else -1)