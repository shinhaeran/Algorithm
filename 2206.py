import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# n, m = map(int, input().split())
board = []
# visit = [[0 for _ in range(m)] for _ in range(n)]
# visit_breaked = [[0 for _ in range(m)] for _ in range(n)] #벽 뚫았을 경우 방문 표시 따로 해줘야 함 -> 왜냐? visit하나로 하면 방문 한번만 하기 때문에 제대로 안됨
# for y in range(n):
#     for s in input():
#         board[y].append(s)
for i in range(n):
    board.append(list(map(int, list(input().strip()))))
def bfs():
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    

    from collections import deque
    q = deque()
    # q.appendleft((0,0,False))
    q.append([0, 0, 1])
    # visit[0][0] = 1
    visit[0][0][1] = 1

    dx = [0,-1,1,0]
    dy = [-1,0,0,1]

    while q:
        x,y,flag = q.pop()
        if x == m-1 and y== n-1:
            return visit[y][x][flag]
        
        for i in range(4):
            if 0 <= x+dx[i] <m and 0<= y+dy[i] < n:
                # if board[y+dy[i]][x+dx[i]] == '0':#일단 뚫린 길 방문
                #     if flag == False and visit[y+dy[i]][x+dx[i]]==0: #아직 벽 뚫지 x 상태
                #         q.appendleft((x+dx[i],y+dy[i],flag))
                #         visit[y+dy[i]][x+dx[i]] = visit[y][x] + 1
                #     elif flag == True and visit_breaked[y+dy[i]][x+dx[i]] == 0:#벽 뚫은 상태
                #         q.appendleft((x+dx[i],y+dy[i],flag))
                #         visit_breaked[y+dy[i]][x+dx[i]] = visit_breaked[y][x] + 1

                # elif board[y+dy[i]][x+dx[i]] == '1' and flag == False and visit[y+dy[i]][x+dx[i]] == 0:#벽 뚫는 순간
                #     q.appendleft((x+dx[i],y+dy[i],True))
                #     visit_breaked[y+dy[i]][x+dx[i]] = visit[y][x] + 1
                if board[y+dy[i]][x+dx[i]] == 1 and flag == 1:
                    visit[y+dy[i]][x+dx[i]][0] = visit[y][x][1] + 1
                    q.appendleft([x+dx[i],y+dy[i],0])
                elif board[y+dy[i]][x+dx[i]] == 0 and flag == 0:
                    visit[y+dy[i]][x+dx[i]][flag] = visit[y][x][flag] + 1
                    q.appendleft([x+dx[i],y+dy[i],flag])
    return -1
# if visit[n-1][m-1][0] == 0 and visit[n-1][m-1][1] == 0:
#     print('-1')
# elif n-1 == 0 and m-1 == 0 and board[n-1][m-1] == '1':
#     print('-1')
# else:
#     if visit[n-1][m-1][0] == 0:
#         print(visit[n-1][m-1][1])
#     elif visit[n-1][m-1][1] == 0:
#         print(visit[n-1][m-1][0])
#     else:
#         print(min(visit[n-1][m-1][0],visit[n-1][m-1][1]))

print(bfs())

