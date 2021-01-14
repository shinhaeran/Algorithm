def solution(n, times):
    answer = 0
    left,right = 1, min(times)*n
    
    while left<=right:
        mid = (left+right) //2 # 한 심사관에게 주어진 시간
        result_people = 0 # 심사 완료한 사람 수 
        
        for t in times:
            result_people += mid//t
            if result_people > n:
                break
        # print(left,right,mid,result_people)
        if result_people >= n:
            right = mid-1
            answer = mid
        elif result_people < n:
            left = mid+1
        
        
    return answer