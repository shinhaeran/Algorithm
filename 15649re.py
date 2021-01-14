n, pair = map(int,input().split())
num_list = list(i+1 for i in range(n)) # 1,2,3,4
visit = [False]*n
arr = list()

def nm(cnt):
    if cnt == pair:
        print(*arr)
    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        arr.append(num_list[i])
        nm(cnt+1)
        arr.pop()
        visit[i]= False

nm(0)