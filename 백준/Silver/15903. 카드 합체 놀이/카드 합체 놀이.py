import heapq
n,m = map(int,input().split()) # 카드의 개수, 카드 합체를 몇번
card = list(map(int,input().split()))
heapq.heapify(card)

for _ in range(m): # m만큼 반복
    a=heapq.heappop(card)
    b=heapq.heappop(card)
    total=a+b
    heapq.heappush(card,total)
    heapq.heappush(card,total)

print(sum(card))