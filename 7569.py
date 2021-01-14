w,h,d =map(int,input().split()) #width, height, depth
board = [[[]for _ in range(h)] for _ in range(d)]
# print(board)
from collections import deque
q = deque()
ripe_num,wall_num = 0,0
for i in range(d):
    for j in range(h):
        s = input().split()
        for k in range(len(s)):
            board[i][j].append(int(s[k]))
            if s[k] == '1':
                q.appendleft((i,j,k)) #z,y,x
                ripe_num += 1
            elif s[k] == '-1':
                wall_num += 1
# print(q)
dz = [0,-1,0,0,1,0]
dy = [1,0,0,-1,0,0]
dx = [0,0,1,0,0,-1]
days = -1
while q:
    for _ in range(len(q)):
        z,y,x = q.pop()
        for i in range(6):
            if 0 <= z+dz[i] < d and 0<= y+dy[i] <h and 0<= x+dx[i]<w and board[z+dz[i]][y+dy[i]][x+dx[i]] == 0:
                q.appendleft((z+dz[i],y+dy[i],x+dx[i]))
                board[z+dz[i]][y+dy[i]][x+dx[i]] =  board[z][y][x] + 1
                ripe_num += 1
    days += 1

if w*h*d - wall_num == ripe_num:
    print(days)
else:
    print('-1')
    # print(ripe_num,wall_num)



