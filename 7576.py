n,m = map(int, input().split())
board = list()
for i in range(m):
    board.append(list(map(int,input().split())))

from collections import deque
q = deque()
# q.appendleft((start_x,start_y))

#bfs의 경우, 출발지가 여러개인 경우에 초기 queue에 익어있는 토마토를 전부 넣어서 동시에 돌리면 된다. 굳이 하나 돌리고 하나돌리고 할 필요 x
ripe_cnt = int()
wall_cnt = int()
visit = [[False for _ in range(n)] for _ in range(m)]
for y in range(m):
    for x in range(n):
        if board[y][x] == 1:
            q.appendleft((x,y))
            ripe_cnt += 1
            visit[y][x] = 1
        elif board[y][x] == -1:
            wall_cnt += 1


def bfs(q):
    
    global ripe_cnt,visit
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]
    bfs_cnt = int()
    yy,xx = int(),int()
    while q:
        x,y = q.pop()
        bfs_cnt += 1
        for i in range(4):
            if y+dy[i] >= 0 and x+dx[i] >= 0 and y+dy[i] < m and x+dx[i] < n:
                # if board[y+dy[i]][x+dx[i]] != -1 and visit[y+dy[i]][x+dx[i]] == False:
                if board[y+dy[i]][x+dx[i]] == 0:
                    q.appendleft((x+dx[i],y+dy[i]))
                    # visit[y+dy[i]][x+dx[i]] = visit[y][x] + 1
                    board[y+dy[i]][x+dx[i]] = board[y][x] + 1
                    ripe_cnt += 1
                    yy,xx = y+dy[i],x+dx[i]
        if ripe_cnt == (n*m) - wall_cnt: #모든 토마토가 익은 경우
            print(board[yy][xx]-1)
            return
        
    #모든 토마토가 익을 수 없는 경우 -> wall빼고 visit False 있으면 -1로 해야할듯
    print('-1')    

bfs(q)

