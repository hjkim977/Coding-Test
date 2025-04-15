import heapq
import sys
n=int(sys.stdin.readline())
x_heap=[]
max_list=[]

for _ in range(n):
    x=int(sys.stdin.readline())
    heapq.heappush(x_heap,-x)
    if x==0:
        r=heapq.heappop(x_heap)
        max_list.append(str(-r))

print("\n".join(max_list))