from collections import deque
def bfs(w,h,board,q):
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]
    
    while(q):
        x, y = q.pop()
        # if board[y][x] != 1:
        #     continue
        for i in range(4):
            if 0 <= x+dx[i] <w and 0<= y+dy[i] < h:
                if board[y+dy[i]][x+dx[i]] == 1:
                    q.appendleft((x+dx[i],y+dy[i]))
                    board[y+dy[i]][x+dx[i]] = board[y][x]
                    
    # print(board)
    
    

n = int(input())
answer = list()
for _ in range(n):
    w,h,worm_num = map(int,input().split())
    board = [[0 for _ in range(w)] for _ in range(h)]
    q = deque()
    for _ in range(worm_num):
        x,y = map(int,input().split())
        board[y][x] = 1
        # q.appendleft((x,y))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                cnt += 1
                board[i][j] += cnt 
                q.appendleft((j,i))
                bfs(w,h,board,q)
    answer.append(cnt)
for e in answer:
    print(e)
