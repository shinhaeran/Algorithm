
def nm(visit,index,pair,n):
    global graph
    visit.append(index)
    if len(visit)==pair:
        for v in visit:
            print(v+1,end=' ')
        print()
        return 
    
    for i in range(n):
        if graph[index][i] == 1 and i not in visit:
            # visit.append(i)
            nm(list(visit),i,pair,n)


n, pair = map(int,input().split())

graph = [ [1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            graph[i][j] = 0

visit = list()
for i in range(n):
    # visit.append(i)
    nm(visit,i,pair,n)
    visit.clear()