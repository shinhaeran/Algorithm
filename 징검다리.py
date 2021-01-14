def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right = 0,distance
    #돌과 돌 사이의 거리가 이분탐색 기준값보다 작을 경우, 뒤쪽 돌을 삭제
    #삭제한 돌의 갸수가 기준 n보다 클 경우 돌과 돌 사이의 거리를 줄이고, n보다 작거나 같을 경우 거리를 늘리는 식으로 이분탐색
    while left <= right:
        mid = (left+right)//2 # 이분탐색 기준값
        delete_cnt = 0
        prev = 0
        for i in range(len(rocks)): # [2,11,14,17,21]
            if rocks[i] - prev < mid:
                delete_cnt += 1
            else:
                prev = rocks[i]
            # print(i,prev,rocks[i]-prev,delete_cnt)
        
        if delete_cnt > n: #mid를 작게 -> right를 작게
            right = mid -1
        else: #delete_cnt <= n
            left = mid +1
            answer = mid
            
                
            
            
        
    return answer