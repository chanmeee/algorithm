# 섞은 음식의 스코빌 지수 = 최소 스코빌 지수 + (두 번째로 최소 스코빌 지수 * 2) 
# 모든 음식이 스코빌 K 이상이 될 때까지 반복
# 만들 수 없는 경우에는 -1을 return

def solution(scoville, K):
    
    import heapq 
    heap = []
    for i in scoville: 
        heapq.heappush(heap, i)
    answer = 0
    
    while (heap[0] < K ): 
        
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return  -1
        answer += 1 
        
    return answer



