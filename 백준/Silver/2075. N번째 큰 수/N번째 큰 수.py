import heapq
n = int(input())
heap = []
for m in range(n):
    graph = list(map(int,input().split()))
    for g in graph:
        if m==0:
            heapq.heappush(heap,g)
        else:
            if heap[0]<g:
                heapq.heappop(heap)
                heapq.heappush(heap,g)
print(heap[0])