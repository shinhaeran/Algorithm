n = int(input())
import math
cost = [[math.inf for _ in range(n+1)] for _ in range(n+1)]
city_path = [set() for _ in range(n+1)]
for _ in range(int(input())):
    s,d,c = map(int,input().split())
    cost[s][d] = min(c,cost[s][d])
    # city_path[s].add(d)

# for i in range(1,n+1): #i
#     temp = set()
#     for j in city_path[i]: # i->j
#         for k in city_path[j] :# j->k => i->k
#             if i==k:
#                 continue
#             cost[i][k] = min(cost[i][k],cost[i][j]+cost[j][k])
#             temp.add(k)
#     city_path[i].update(temp)
for j in range(1,n+1): # i->j->k
    for i in range(1,n+1):
        for k in range(1,n+1):
            if i == k:
                continue
            cost[i][k] = min(cost[i][k],cost[i][j]+cost[j][k])
for i in range(1,n+1):
    for e in cost[i][1:]:
        if e == math.inf:
            print(0,end=' ')
        else:
            print(e,end=' ')
    print()






        