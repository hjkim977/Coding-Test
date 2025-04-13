'''최소힙: 부모노드 값이 자식노드 값보다 항상 작다
   최대힙: 부모노드 값이 자식노드 값보다 항상 크다
heapq는 최소 힙으로만 구성 / 최대힙을 구하려면 원래 값에 -1을 곱해 최대값이 최소가 되도록 구현'''
import heapq
def solution(operations):
    min_h=[]
    max_h=[]
    num={} #숫자 개수 저장
    
    for o in operations:
        t,n = o.split() # t:I/D
        n=int(n)
        
        if t=="I":
            heapq.heappush(min_h, n)
            heapq.heappush(max_h, -n)
            if num.get(n):
                num[n] += 1
            else:
                num[n] = 1
            
        else:
            if n==1: # 최대값 삭제
                if len(max_h):
                    add = -heapq.heappop(max_h)
                else:
                    continue
                while max_h and num[add] < 1:
                    add = -heapq.heappop(max_h)
                num[add] -=1
            
            else: # 최소값 삭제
                if len(min_h):
                    add=heapq.heappop(min_h)
                else:
                    continue
                while min_h and num[add] < 1:
                    add = heapq.heappop(min_h)
                num[add]-=1

    while min_h and num[min_h[0]]<1:
        heapq.heappop(min_h)
    min=min_h[0] if len(min_h) else 0

    while max_h and num[-max_h[0]]<1:
        heapq.heappop(max_h)
    max=-max_h[0] if len(max_h) else 0

    return [max,min]