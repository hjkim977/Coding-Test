import heapq
import sys
input=sys.stdin.readline
n = int(input())
c = [tuple(map(int, input().split())) for _ in range(n)]

c.sort()  # 시작 시간 기준 정렬
heap = []

for s, e in c:
    if heap and heap[0] <= s:
        heapq.heappop(heap)  # 이전 강의실 끝났으니 재사용
    heapq.heappush(heap, e)  # 새 강의 or 재사용된 강의실에 종료 시간 추가

print(len(heap))
