def solution(numbers, target):
    answer = 0
    from collections import deque
    num = int()
    q = deque()
    q.appendleft((numbers[0],0))
    q.appendleft((-numbers[0],0))
    
    while q:
        n,index = q.pop()
        if index >= len(numbers)-1:
            if n == target:
                answer += 1
        else:
            q.appendleft((n+numbers[index+1],index+1))
            q.appendleft((n-numbers[index+1],index+1))
    
    
    return answer