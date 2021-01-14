n,k = map(int,input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n)]
pack = []
for _ in range(n):
    w,v = map(int,input().split())
    pack.append((w,v))

for i in range(pack[0][0],k+1):
    dp[0][i] = pack[0][1]

for i in range(1,n): # 1 ~ 3
    for j in range(1,k+1): # 0~6 pack[i][0] : w , pack[i][1] : v
        if j-pack[i][0] >= 0 :
            temp =  dp[i-1][j-pack[i][0]]+pack[i][1]
            # print(i,j,temp)
        else:
            temp = 0
        dp[i][j] = max(dp[i-1][j],temp) 
# print(dp)
print(dp[n-1][k])
