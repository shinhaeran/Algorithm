source, destination = map(int, input().split())
board = [i for i in range(100001)]
visit = [False for _ in range(100001)]

from collections import deque
q = deque()
q.appendleft(source)
visit[source] =  0

while q:
    target = q.pop()

    if target == destination:
        print(visit[target])
        break
    if target-1 >= 0 and not visit[target -1]:
        q.appendleft(target -1)
        visit[target-1] = visit[target] + 1
    if target+1 < 100001 and not visit[target +1]:
        q.appendleft(target +1)
        visit[target+1] = visit[target] + 1
    if target*2 < 100001 and not visit[target*2]:
        q.appendleft(target*2)
        visit[target*2] = visit[target] + 1



