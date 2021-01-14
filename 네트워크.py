def solution(n, computers):
    answer = 0
    from collections import deque
    q = deque()
    
    visit = [False for _ in range(n)]
    for j in range(n):
        if visit[j] == False:
            q.appendleft(j)
            visit[j] = True
            while q:
                node = q.pop()

                for i in range(n):
                    if computers[node][i]==1 and visit[i] == False:
                        visit[i] = True
                        q.appendleft(i)
            answer += 1
    return answer