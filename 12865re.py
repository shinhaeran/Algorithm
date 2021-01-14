# n, target_weight = map(int, input().split())
# dp = [[0 for _ in range(target_weight+1)] for _ in range(n)]
# pack = []

# for _ in range(n):
#     w,v = map(int, input().split())
#     pack.append((w,v))

# def packing():
#     temp = int()
#     for i in range(pack[0][0],target_weight+1):
#         dp[0][i] = pack[0][1]
#     for i in range(1,n):
#         for j in range(1,target_weight+1):
#             if  j-pack[i][0] >= 0:
#                 temp = dp[i-1][j-pack[i][0]]+pack[i][1]
#                 # print('aa',temp,i,j)
#             # if pack[i][0] <= j:
#             #     temp = pack[i][1]
#             else:
#                 temp = 0 
#             dp[i][j] = max(temp,dp[i-1][j],dp[i][j-1])
# packing()
# print(dp[n-1][target_weight])


import sys


(stuffNum, limit) = map(int, sys.stdin.readline().split())
weight = []
values = []
cache = [[-1 for i in range(limit + 1)] for j in range(stuffNum)]


def find_max_val(i, w):
    if cache[i][w] != -1:
        return cache[i][w]
    if i == 0:
        tmp = values[0] if w >= weight[0] else 0
        cache[i][w] = tmp
        return tmp
    if weight[i] > w:
        return find_max_val(i - 1, w)
    tmp = max(find_max_val(i - 1, w), find_max_val(i - 1, w - weight[i]) + values[i])
    cache[i][w] = tmp
    return tmp


for i in range(stuffNum):
    (x, y) = map(int, sys.stdin.readline().split())
    weight.append(x)
    values.append(y)

print(find_max_val(stuffNum - 1, limit))
