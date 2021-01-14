n = int(input())
board = [[] for _ in range(n)]
for j in range(n):
    for i in input():
        board[j].append(int(i))
visit = [[False for _ in range(n)] for _ in range(n)]
dfs_num = 0
def dfs(cnt,y,x):
    global dfs_num
    dfs_num += 1
    visit[y][x] = True
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]
    
    for i in range(4):
        if y+dy[i] >= 0 and x+dx[i] >= 0 and y+dy[i] < n and x+dx[i] < n:
            if board[y+dy[i]][x+dx[i]] ==  1 and visit[y+dy[i]][x+dx[i]] == False:
                dfs(cnt+1,dy[i]+y,dx[i]+x)
    
                    
    
answer = list()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visit[i][j] == False:
            dfs(1,i,j)
            answer.append(dfs_num)
            dfs_num  = 0

print(len(answer))
answer.sort()
for i in answer:
    print(i)





