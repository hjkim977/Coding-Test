n, m = map(int, input().split())
books = list(map(int, input().split()))

pos_li = []
neg_li = []
furthest = 0
result = 0

for book in books:
    furthest = max(abs(book), furthest)
    if book > 0:
        pos_li.append(book)
    else:
        neg_li.append(abs(book))

pos_li.sort(reverse=1)
neg_li.sort(reverse=1)

for i in range(0, len(pos_li), m):
    result += pos_li[i] * 2

for i in range(0, len(neg_li), m):
    result += neg_li[i] * 2

print(result - furthest)