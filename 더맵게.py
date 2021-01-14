import heapq
def solution(scoville, K):
    heapq.heapify(scoville) #min_heap
    cnt  =  0
    while scoville:
        try:
            a=heapq.heappop(scoville)
            if a >= K:
                return cnt
            cnt += 1
            b = heapq.heappop(scoville)
            heapq.heappush(scoville,a+(b*2))
        except:
            break
        
    return -1