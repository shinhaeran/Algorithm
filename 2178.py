#dfs로 푼거 
n,m = map(int,input().split())
load = list()
for _ in range(n):
    load.append(input())
visit = [[False for _ in range(m)] for _ in range(n)]

answer = 9999999

def find_exit(x,y,cnt):
    global answer
    if x==m-1 and y==n-1:
        answer = min(answer,cnt)
        return 
    visit[y][x] = True
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]

    for i in range(4):
        if 0 <= x+dx[i] <m and 0<= y+dy[i] < n:
            if load[y+dy[i]][x+dx[i]] == '1' and visit[y+dy[i]][x+dx[i]] == False:
                find_exit(x+dx[i],y+dy[i],cnt+1)
                visit[y+dy[i]][x+dx[i]] = False
find_exit(0,0,1)
print(answer)
