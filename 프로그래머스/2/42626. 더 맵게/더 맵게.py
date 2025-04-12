#이진 트리 기반의 최소힙(부모 노드가 자식 노드보다 항상 작은 값을 가짐) 자료구조 만을 제공한다.

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 리스트를 힙으로 변환
    count = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1  # 더 이상 섞을 수 없는데 K 못 넘으면 실패
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_food = first + (second * 2)
        heapq.heappush(scoville, new_food)
        count += 1

    return count
