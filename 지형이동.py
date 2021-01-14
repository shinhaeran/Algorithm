def find_diff(y,x,Y,X,board,land,land_diff):
    if board[y][x] != board[Y][X]:
        land_diff[board[y][x]][board[Y][X]] = min(abs(land[y][x]-land[Y][X]),land_diff[board[y][x]][board[Y][X]])
        land_diff[board[Y][X]][board[y][x]] = land_diff[board[y][x]][board[Y][X]]    
def solution(land, height):
    answer = 0
    from collections import deque
    q = deque()
    q.appendleft((0,0))
    
    dx = [0,0,-1,+1]
    dy = [1,-1,0,0]
    import math
    board = [[math.inf for _ in range(len(land))] for _ in range(len(land))]
    board[0][0] = 0
    cnt = 0
    while q:
        x,y = q.pop()
        for i in range(4):
            X,Y=x+dx[i],y+dy[i]
            if not 0<=X<len(land) or not 0<=Y<len(land):
                continue
            if board[y][x] < board[Y][X]:
                q.appendleft((X,Y))
                if abs(land[y][x] - land[Y][X]) <= height:
                    board[Y][X] = min(board[y][x],board[Y][X])
                    board[y][x] = board[Y][X]
                else:
                    if board[Y][X] == math.inf:
                        board[Y][X] = board[y][x]+1
                    else:
                        board[Y][X] = max(board[y][x]+1,board[Y][X])
                cnt = max(cnt,board[Y][X])
                        
    land_diff = [[math.inf for _ in range(cnt)] for _ in range(cnt)]
    for y in range(len(land)-1):
        for x in range(len(land)-1):
            find_diff(y,x,y+1,x,board,land,land_diff)
            find_diff(y,x,y,x+1,board,land,land_diff)
    # find_diff(len(land)-1,len(land)-1,len(land)-2,len(land)-1,board,land,land_diff)
    print(board)
    print(land_diff)
            
    return answer
solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3)