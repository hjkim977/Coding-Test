import heapq,sys
input = sys.stdin.readline

n, m = map(int,input().split())
time = list(map(int,input().split()))
time.sort(reverse=True) # 시간이 오래 걸리는 순서대로 콘센트에 먼저 꽂기

heap = [0]*m

for t in time:
    min_time = heapq.heappop(heap) # 가장 작은 값이 제거됨
    heapq.heappush(heap, min_time+t)
print(max(heap))