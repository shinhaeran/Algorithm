n = int(input())
cost = list()
for _ in range(n):
    cost.append(int(input()))
dp = cost.copy()
visit = [False for _ in range(n)]
visit
try:
    dp[1] = cost[0]+cost[1]
    dp[2] = max(cost[0]+cost[2],cost[1]+cost[2])
except:
    pass
for i in range(3,n):
    # if visit[i-1] and visit[i-2]:
    #     dp[i] = max(dp[i-1],dp[i-2]+cost[i])
    #     if dp[i] == dp[i-2]+cost[i]:
    #         visit[i] = True
    # else:
    #     dp[i] = max(dp[i-1]+cost[i],dp[i-2]+cost[i])
    #     visit[i] = True
    dp[i] = max(dp[i-3]+cost[i-1]+cost[i],dp[i-2]+cost[i])

# print(visit,dp)
print(dp[n-1])