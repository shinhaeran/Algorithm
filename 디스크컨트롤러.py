import heapq as hq
from collections import deque
def solution(jobs):
    answer = 0
    jobs = deque(sorted(jobs,key=lambda x : (x[0],x[1])))
    
    N = len(jobs)
    current =  0#현재 시간
    wait = 0 #대기시간
    candidates = []
    cnt = 0
    # total_running_time = 0
    # for i in range(N):
    #     total_running_time += jobs[i][1]
    
    while cnt < N:
        if candidates: # 이 안에서 heap 돌리면서 수행
            while candidates:
                if len(jobs) >0 and jobs[0][0] <= current:
                    break
                r,w = hq.heappop(candidates)
                wait += current - w + r
                current += r
                cnt += 1
                
        else: # jobs[0]을 수행
            w,r=jobs.popleft()
            wait += r
            current = w+r
            cnt += 1
            
        
        while jobs:#candidates 선별
            if current >= jobs[0][0]:
                hq.heappush(candidates, jobs.popleft()[::-1])
            else:
                break
    
    answer = (wait) // N
    return answer