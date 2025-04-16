import heapq, sys
n=int(sys.stdin.readline())
s_heap=[]
for _ in range(n):
    list=map(int,sys.stdin.readline().split())
    for l in list:
        if len(s_heap)<n:
            heapq.heappush(s_heap,l)
        else:
            if s_heap[0]<l:
                heapq.heappop(s_heap)
                heapq.heappush(s_heap,l)
print(s_heap[0])