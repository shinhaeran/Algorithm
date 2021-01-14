# bfs로 푼거
n,m = map(int,input().split())
load = list()
for _ in range(n):
    load.append(input())
visit = [[False for _ in range(m)] for _ in range(n)]



def find_exit():
    # answer = 9999999
    from collections import deque
    bfs_que = deque()
    bfs_que.appendleft((0,0))
    # cnt = 0
    visit[0][0] = 1
    
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]

    while(len(bfs_que)>0):
        x,y = bfs_que.pop()
        # visit[y][x] = True
        # cnt += 1
        if x==m-1 and y==n-1:
            print(visit[y][x])
            # answer = min(answer,cnt)
            # cnt = 0
            break
        
        for i in range(4):
            if 0 <= x+dx[i] <m and 0<= y+dy[i] < n:
                if load[y+dy[i]][x+dx[i]] == '1' and visit[y+dy[i]][x+dx[i]] == False:
                    bfs_que.appendleft((x+dx[i],y+dy[i]))
                    visit[y+dy[i]][x+dx[i]] = visit[y][x] + 1
    print(visit)
    # queue로 이어진 곳을 먼저 선점해서 +1 하고 visit 표시 하기 때문에 재방문이 없어 최단거리 가능 !!
find_exit()

