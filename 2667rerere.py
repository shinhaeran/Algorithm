# bfs로 푼 거 
n = int(input())
board = [[] for _ in range(n)]
for i in range(n):
    for e in input():
        board[i].append(int(e))
visit = [[False for _ in range(n)] for _ in range(n)]
answer = list()
def bfs(start_x,start_y):
    global visit
    from collections import deque
    q = deque()
    q.appendleft((start_x,start_y))
    visit[start_y][start_x] = True
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]
    cnt = 1
    while(q):
        x,y = q.pop()

        for i in range(4):
            if y+dy[i] >= 0 and x+dx[i] >= 0 and y+dy[i] < n and x+dx[i] < n:
                # if board[y+dy[i]][x+dx[i]] == 1 and visit[y+dy[i]][x+dx[i]] == False:
                    q.appendleft((x+dx[i],y+dy[i]))
                    visit[y+dy[i]][x+dx[i]] = True
                    cnt += 1
    answer.append(cnt)    
bfs_cnt = 0
for y in range(n):
    for x in range(n):
        if board[y][x] == 1 and visit[y][x] == False:
            bfs_cnt += 1
            bfs(x,y)
answer.sort()
print(bfs_cnt)
for e in answer :
    print(e)