import heapq,sys
n=int(sys.stdin.readline())
x_heap=[]
result=[]

for _ in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if x_heap:
            r=heapq.heappop(x_heap)
            result.append(str(r))
        else:
            result.append(str(0))
    else:
        heapq.heappush(x_heap,x)

print("\n".join(result))