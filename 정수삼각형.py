# node의 간선이 그래프의 크기 n-1이라면 순위 확실 -> 서브그래프 탐색 반복
def rank(players,graph_win,graph_lose,confirmed):
    
    if len(players) == 1:
        confirmed[players[0]] = True
        return confirmed.count(True)
    result = 0
    for i in players:
        if len(graph_win[i]) + len(graph_lose[i]) == len(players)-1:
            confirmed[i] = True
            for j in graph_win[i]:
                graph_lose[j].remove(i)
            for j in graph_lose[i]:
                graph_win[j].remove(i)
        
            result = max(rank(graph_win[i],graph_win,graph_lose,confirmed),rank(graph_lose[i],graph_win,graph_lose,confirmed))
            
            
    
    return result
                   
            
def solution(n, results):
    answer = 0
    graph_win = [[] for _ in range(n+1)]
    graph_lose = [[] for _ in range(n+1)]
    for r in results:
        graph_win[r[0]].append(r[1]) #r0이 r1에게 이겼다
        graph_lose[r[1]].append(r[0]) #s1이 r0에게 졌다
    
    
    answer=rank([i+1 for i in range(n)],graph_win,graph_lose,[False for _ in range(n+1)])
                
            
    return answer
solution(5,[[1, 2], [2, 5], [2, 4], [3, 2], [4, 5]])
