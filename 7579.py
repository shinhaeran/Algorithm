n,target = map(int,input().split())
m = [0]+list(map(int,input().split()))
c = [0]+list(map(int,input().split()))

apps = []
for i in range(n):
    apps.append((m[i],c[i]))
# result = 99999999999
result = sum(c)
dp = [[0 for _ in range(sum(c)+1)] for _ in range(n+1)]  #dp[i][j] : i번째 app이 j메모리로 비활성화하는 cost의 최솟값 -> result
# for i in range(c[1],sum(c)+1):
#     dp[0][i] = m[1]

for i in range(1,n+1):
    for j in range(1,sum(c)+1):
        if c[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-c[i]]+m[i])
        if dp[i][j] >= target:
            result = min(result,j)

if target == 0:
    print(0)
else:
    print(result)
