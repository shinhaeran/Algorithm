n,m = map(int, input().split())
board = [[] for i in range(n)]
for i in range(n):
    for e in input():
        board[i].append(int(e))
# print(board)

visit = [[False for _ in range(m)] for _ in range(n)]
visit[0][0] = 1
from collections import deque
q = deque()
q.appendleft((0,0))
dx = [0,1,0,-1]
dy = [-1,0,1,0]
while(q):
    x,y = q.pop()
    if x==m-1 and y==n-1:
        print(visit[y][x])
        break
    for i in range(4):
        if 0<=x+dx[i]<m and 0<=y+dy[i]<n:
            if board[y+dy[i]][x+dx[i]] == 1 and visit[y+dy[i]][x+dx[i]] == False:
                q.appendleft((x+dx[i], y+dy[i]))
                visit[y+dy[i]][x+dx[i]] = visit[y][x] + 1
# print(visit[n-1][m-1])

