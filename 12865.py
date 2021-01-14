n, target_weight = map(int,input().split())

w = []
v =[]
dp = [[0 for _ in range(target_weight+1)] for _ in range(n)]

for _ in range(n):
    weight,value = map(int,input().split())
    w.append(weight)
    v.append(value)

for i in range(w[0],target_weight+1):
    dp[0][i] = v[0]
for i in range(1,n):
    flag = False
    for j in range(target_weight+1):
        if 0 <= j - w[i]:
            if flag:
                temp = dp[i][j-1]
            else:
                temp = dp[i][j-w[i]]+v[i]
                flag = True
        else:
            temp = 0
        print(temp,flag)
        dp[i][j] = max(dp[i-1][j], temp)
# print(dp[n-1][target_weight])
# print(dp)


