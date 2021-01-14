def solution(n, results):
    answer = 0
    win = [set() for _ in range(n+1)]
    lose = [set() for _ in range(n+1)]
    for w,l in results:
        win[w].add(l) # w이 이긴애들 
        lose[l].add(w) # l이 진 애들
        
    for i in range(1,n+1):
        for loser in win[i]: # i한테 진 애들은 i가 진애들한테도 진다
            lose[loser].update(lose[i])
        for winner in lose[i]: #i한테 이긴 애들은 i가 진 애들한테도 이긴다
            win[winner].update(win[i])
            
    cnt = 0
    for i in range(1,n+1):
        if len(lose[i]) + len(win[i]) == n-1:
            cnt += 1
    answer = cnt
    return answer