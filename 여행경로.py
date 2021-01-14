import copy
def find_path(graph,s,visit,N):
    print(graph,visit,s)
    if len(visit) == N+1:
        return visit
    
    for idx, dst in enumerate(graph[s]):
        visit_temp = visit[:]
        visit_temp.append(dst)
        graph[s].pop(idx)
        result = find_path(graph,dst,visit_temp,N)
        graph[s].insert(idx,dst)
        if result:
            return result
    
def solution(tickets):
    answer = []
    from collections import defaultdict
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    for key in graph.keys():
        graph[key].sort()
    answer = find_path(graph,"ICN",["ICN"],len(tickets))
    
    
    return answer