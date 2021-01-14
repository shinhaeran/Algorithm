def union(a,b,parent):
    pa,pb = find_parent(a,parent),find_parent(b,parent)
    parent[a] = min(pa,pb)
    parent[b] = min(pa,pb)
def find_parent(n,parent):
    if n == parent[n]:
        return n
    parent[n] = find_parent(parent[n],parent)
    return parent[n]
def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    cnt = 0
    costs.sort(key=lambda x:x[2])
    for i in range(len(costs)):
        pa,pb = find_parent(costs[i][0],parent),find_parent(costs[i][1],parent)
        if pa != pb:
            cnt += 1
            answer += costs[i][2]
            union(pa,pb,parent)
        if cnt == n-1:
            break
    return answer