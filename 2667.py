n = int(input())
board = [[] for _ in range(n)]
for j in range(n):
    for i in input():
        board[j].append(int(i))
visit = [[False for _ in range(n)] for _ in range(n)]

# def dfs(cnt,x,y):
#     # global cnt
#     try:
#         if board[y+1][x] == 1 and visit[y+1][x]== False:
#             visit[y+1][x] = True
#             dfs(cnt+1,x,y+1)
#     except:
#         pass
#     try:
#         if board[y][x+1] == 1 and visit[y][x+1]== False:
#             visit[y][x+1] = True
#             dfs(cnt+1,x+1,y)
#     except:
#         pass
#     try:
#         if board[y-1][x] == 1 and visit[y-1][x]== False:
#             visit[y-1][x] = True
#             dfs(cnt+1,x,y-1)
#     except:
#         pass
#     try:
#         if board[y][x-1] == 1 and visit[y][x-1]== False:
#             visit[y][x-1] = True
#             dfs(cnt+1,x-1,y)
#     except:
#         pass
#     return cnt
def dfs(visit,cnt, x,y):
    visit[y][x]=True
    # 이건 이제 이미 간것이다. 하고 0으로 바꾸는것 이다.
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        # 이 근처 다 n_x, n_y로 간다.
        if n_x>=0 and n_x<n and n_y>=0 and n_y<n:
            # 범위 check
            if board[n_y][n_x]==1 and visit[n_y][n_x]==False:
            # 그부분이 1이면
                cnt = dfs(visit,cnt+1, n_x, n_y)
                # cnt를 증가시켜서 다시한번 그 근처 확인
    return cnt
    # 다 cnt검사하면 끝을 낸다.
ans =[]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visit[i][j] == False:
            ans.append(dfs(visit,0,j,i))
for i in ans:
    print(i)
